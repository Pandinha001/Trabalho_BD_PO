from random import choice
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from Pele import Pele
from Utero import Utero


class Organismo(Base):
    __tablename__ = 'organismo'

    id_avatar = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    idade = Column(Integer, nullable=False)
    peso = Column(Numeric(10, 2, asdecimal=False), nullable=False)   # float em vez de Decimal
    energia = Column(Integer, nullable=False)
    intensidade_dor = Column(Integer, nullable=False)
    fome = Column(Integer, nullable=False)

    id_bioma = Column(Integer, ForeignKey('bioma.id_bioma'), nullable=False)
    bioma = relationship('Bioma', back_populates='organismos')                       # N:1
    pele = relationship('Pele', back_populates='organismo', uselist=False)           # 1:1
    utero = relationship('Utero', back_populates='organismo', uselist=False)         # 1:1

    def __init__(self, nome, idade, peso, bioma):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.energia = 100
        self.intensidade_dor = 0
        self.fome = 0
        self.bioma = bioma                                  # objeto Bioma (e não a classe)
        self.pele = Pele(melanina=choice(["baixa", "media", "alta"]))
        self.utero = Utero()

    def _ajustar_limites(self):
        self.energia = max(0, min(100, self.energia))
        self.fome = max(0, min(100, self.fome))

    def movimentar(self, distancia: float):
        print(f"🏃 {self.nome} começou a se movimentar no bioma {self.bioma.nome}")
        gasto = self.bioma.dificuldade_solo() * distancia
        if self.peso >= 70:
            quilos_extras = self.peso - 70
            gasto += gasto * (quilos_extras * 0.01)
        self.energia -= int(gasto)
        self._ajustar_limites()
        print(f"⚡ Gasto de energia. Energia atual: {self.energia}")

    def hidratar(self, escolha):
        if escolha == 1:
            self.energia += 10
            print(f"Parabéns, {self.nome}! Você bebeu 200ml de água potável!")
        elif escolha == 2:
            self.energia += 15
            print(f"Maravilha! {self.nome} Você bebeu 200ml de água de coco!")
        elif escolha == 3:
            self.energia -= 15
            print(f"Que nojo! {self.nome} você bebeu 200ml de água suja!")
        else:
            print("Opção inválida! Você não bebeu nada.")
            self.energia -= 10
        self._ajustar_limites()

    def alimentar(self, escolha):
        if escolha == 1:
            self.energia -= 15
            self.fome += 5
            print(f"Ops! {self.nome} tinha opção melhor hein.")
        elif escolha == 2:
            self.energia += 5
            self.fome -= 5
            print("Foi quase hein! Boa sorte na próxima.")
        elif escolha == 3:
            self.energia += 15
            self.fome -= 10
            print("Opção incrível!! Parabéns")
        else:
            print("Opção inválida! Você não comeu nada.")
            self.fome += 15
            self.energia -= 15
        self._ajustar_limites()

    def fazer_nada(self):
        if self.energia >= 10:
            self.energia -= 10
            print(f"Deu mole, perdeu energia. Energia atual {self.energia}")
        else:
            self.energia = 0

        if self.energia == 0:
            if self.fome >= 100:
                print(f"Você está sem energia e com muita fome. {self.nome} não sobreviveu.")
            else:
                print(f"Você está sem energia e com fome. {self.nome} melhor comer e se hidratar.")

    def proteger(self, escolha):
        if escolha in (1, 2, 3):
            self.bioma.proteger(self, escolha)      # cada bioma sabe qual item é o correto
        else:
            print("Opção inválida! Você não se protegeu.")
            self.intensidade_dor += 3

    def __repr__(self):
        return f"Organismo({self.id_avatar}, {self.nome!r}, {self.idade})"
