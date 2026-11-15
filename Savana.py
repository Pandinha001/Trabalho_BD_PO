import random
from sqlalchemy import Column, Float
from Bioma import Bioma


class Savana(Bioma):
    __mapper_args__ = {'polymorphic_identity': 'Savana'}
    nivel_queimada = Column(Float)

    def __init__(self, nivel_queimada: int):
        super().__init__(
            nome="Savana",
            clima="Tropical Semiárido",
            regiao="África / América do Sul",
            temp_min=20.0,
            temp_max=40.0,
            especificidade="Estação seca prolongada",
            tipo_solo="Arenoso e poroso (Pobre em nutrientes)",
            id_item_correto=1,          # 1 = Protetor solar
        )
        self.nivel_queimada = nivel_queimada

    def calcular_temperatura(self) -> float:
        temperatura_atual = random.uniform(self.temp_min, self.temp_max)
        temperatura_atual += self.nivel_queimada * 1.5
        return round(temperatura_atual, 1)

    def dificuldade_solo(self) -> float:
        return 1.2 + self.nivel_queimada * 0.1

    def aplicar_efeito_pele(self, organismo, usou_item_certo):
        organismo.pele.tomar_sol(tem_protetor_solar=usou_item_certo)

    def exibir_dados(self):
        super().exibir_dados()
        print(f"| Nível de queimada: {self.nivel_queimada} |")
