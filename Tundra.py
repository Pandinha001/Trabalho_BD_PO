import random
from sqlalchemy import Column, Float
from Bioma import Bioma


class Tundra(Bioma):
    __mapper_args__ = {'polymorphic_identity': 'Tundra'}
    espessura_neve = Column(Float)      # coluna só desta subclasse

    def __init__(self, espessura_neve: float = 20.0):
        super().__init__(
            nome="Tundra",
            clima="Frio Polar",
            regiao="Ártico",
            temp_min=-20.0,
            temp_max=0.0,
            especificidade="Periglacial",
            tipo_solo="Permafrost",
            id_item_correto=3,          # 3 = Blusa de frio
        )
        self.espessura_neve = espessura_neve

    def calcular_temperatura(self) -> float:
        temperatura_atual = random.uniform(self.temp_min, self.temp_max)
        return round(temperatura_atual, 1)

    def dificuldade_solo(self) -> float:
        return 1.5 + (self.espessura_neve / 100) * 0.5

    def aplicar_efeito_pele(self, organismo, usou_item_certo):
        organismo.pele.enfrentar_frio(tem_blusa=usou_item_certo)

    def exibir_dados(self):
        super().exibir_dados()
        print(f"| Espessura da neve: {self.espessura_neve} |")
