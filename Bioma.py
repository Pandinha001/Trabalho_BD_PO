from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class TipoProtecao(Base):
    __tablename__ = 'tipo_protecao'
    id_tipo = Column(Integer, primary_key=True, autoincrement=False)
    nome = Column(String(50), nullable=False)
    informacoes = Column(String(100), nullable=False)

    def __repr__(self):
        return f"TipoProtecao({self.id_tipo}, {self.nome!r})"


class Bioma(Base):
    """Classe base. As subclasses (Savana, Tundra, FlorestaTropical) ficam
    TODAS na mesma tabela 'bioma' (herança de tabela única): a coluna 'nome'
    diz de qual subclasse é cada linha."""
    __tablename__ = 'bioma'

    id_bioma = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    clima = Column(String(50), nullable=False)
    regiao = Column(String(50), nullable=False)
    temp_min = Column(Float, nullable=False)
    temp_max = Column(Float, nullable=False)
    especificidade = Column(String(70), nullable=False)
    tipo_solo = Column(String(50), nullable=False)

    # chave estrangeira (coluna real): qual proteção é a correta neste bioma
    id_item_correto = Column(Integer, ForeignKey('tipo_protecao.id_tipo'), nullable=False)
    protecao_correta = relationship('TipoProtecao')                        # N:1
    organismos = relationship('Organismo', back_populates='bioma')         # 1:N

    __mapper_args__ = {'polymorphic_on': nome}

    def __init__(self, nome: str, clima: str, regiao: str, temp_min: float, temp_max: float,
                 especificidade: str, tipo_solo: str, id_item_correto: int):
        self.nome = nome
        self.clima = clima
        self.regiao = regiao
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.especificidade = especificidade
        self.tipo_solo = tipo_solo
        self.id_item_correto = id_item_correto

    # Obs.: não usamos ABC aqui, porque ABCMeta conflita com a metaclasse do
    # SQLAlchemy. O efeito é o mesmo: cada subclasse DEVE sobrescrever estes métodos.
    def calcular_temperatura(self):
        raise NotImplementedError

    def dificuldade_solo(self):
        raise NotImplementedError

    def aplicar_efeito_pele(self, organismo, usou_item_certo):
        raise NotImplementedError

    def proteger(self, organismo, escolha):
        if escolha == self.id_item_correto:
            organismo.intensidade_dor = max(0, organismo.intensidade_dor - 1)
            print("Parabéns, você se defendeu!")
            acertou = True
        else:
            organismo.intensidade_dor += 1
            print("errouu")
            acertou = False

        self.aplicar_efeito_pele(organismo, acertou)

    def exibir_dados(self):
        temp_atual = self.calcular_temperatura()
        print("\n===== DADOS DO BIOMA =====")
        print(f"| Nome: {self.nome} |")
        print(f"| Temperatura: {temp_atual}°C |")
        print(f"| Clima: {self.clima} |")
        print(f"| Região: {self.regiao} |")
        print(f"| Especificidade: {self.especificidade} |")
        print(f"| Tipo do solo: {self.tipo_solo} |")

    def __repr__(self):
        return f"{type(self).__name__}({self.id_bioma}, {self.nome!r})"
