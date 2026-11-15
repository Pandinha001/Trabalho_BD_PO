from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Pele(Base):
    __tablename__ = 'pele'

    # a PK é também a chave estrangeira: relação 1:1 com o organismo
    id_avatar_pele = Column(Integer, ForeignKey('organismo.id_avatar'), primary_key=True)
    melanina = Column(String(10), nullable=False)        # "baixa", "media" ou "alta"
    protecao = Column(Boolean, nullable=False, default=False)

    organismo = relationship('Organismo', back_populates='pele')

    def __init__(self, melanina):
        self.melanina = melanina
        self.protecao = False

    def tomar_sol(self, tem_protetor_solar=False):
        if self.melanina == "baixa":
            if tem_protetor_solar:
                print("✨ Graças ao protetor solar, sua pele sensível está protegida!")
                self.protecao = True
            else:
                print("⚠️ ATENÇÃO: Pele sensível sem protetor solar! Você sofreu queimaduras e insolação.")
                self.protecao = False

        elif self.melanina == "media":
            if tem_protetor_solar:
                print("✨ Com protetor solar, sua pele está super protegida!")
            else:
                print("Você tem proteção moderada, mas o sol da Savana é forte. Cuidado com o tempo de exposição.")
            self.protecao = True

        elif self.melanina == "alta":
            print("✨ Sua pele tem alta proteção natural contra os raios da Savana!")
            self.protecao = True

    def sofrer_picadas(self, tem_repelente=False):
        if tem_repelente:
            print("O repelente afastou os mosquitos!")
            self.protecao = True
        else:
            print("Você foi picado várias vezes!")
            self.protecao = False

    def enfrentar_frio(self, tem_blusa=False):
        if tem_blusa:
            print("A blusa de frio manteve sua pele aquecida!")
            self.protecao = True
        else:
            print("Sua pele está ressecando e congelando!")
            self.protecao = False

    def __repr__(self):
        return f"Pele({self.id_avatar_pele}, {self.melanina!r}, protecao={self.protecao})"
