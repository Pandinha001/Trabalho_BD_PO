from sqlalchemy import select
from Bioma import Bioma
from FlorestaTrop import FlorestaTropical
from Savana import Savana
from Tundra import Tundra
from Organismo import Organismo


class Sistema():
    def __init__(self, session):
        self.session = session

    ### consultas no banco (substituem as antigas listas self.avatares / self.biomas)
    def listar_biomas(self):
        return self.session.scalars(select(Bioma).order_by(Bioma.id_bioma)).all()

    def listar_avatares(self):
        return self.session.scalars(select(Organismo).order_by(Organismo.id_avatar)).all()

    def salvar(self):
        self.session.commit()

    ### criação
    def criar_bioma(self, escolha):
        if escolha == 1:    # floresta tropical
            tipo_solo = input("Informe o tipo do solo: ")
            bioma = FlorestaTropical(tipo_solo)
        elif escolha == 2:  # savana
            nivel_queimada = int(input("Informe o nivel de queimada: "))
            bioma = Savana(nivel_queimada)
        elif escolha == 3:  # tundra
            espessura_neve = float(input("Informe a espessura da neve: "))
            bioma = Tundra(espessura_neve)
        else:
            print("Opção inválida")
            return

        self.session.add(bioma)
        self.session.commit()
        print("Bioma criado com sucesso!")

    def criar_avatar(self, nome, idade, peso, bioma):
        avatar = Organismo(nome, idade, peso, bioma)
        self.session.add(avatar)    # pele e útero entram junto (relationship)
        self.session.commit()

    ### exibição
    def ver_status_saude(self):
        print("\n===== Status de Saúde dos seus Avatares =====\n")
        for avatar in self.listar_avatares():
            print(f"| Nome: {avatar.nome} \n| Idade: {avatar.idade} anos \n| Peso: {avatar.peso} kg \n"
                  f"| Energia: {avatar.energia} \n| Fome: {avatar.fome} \n"
                  f"| Intensidade da dor: {avatar.intensidade_dor}\n")

    def exibir_dados(self):
        for bioma in self.listar_biomas():
            bioma.exibir_dados()    # cada subclasse mostra seus dados extras

    def fazer_funcoes_utero(self):
        for avatar in self.listar_avatares():
            print(f"\nVeja os status do útero do avatar {avatar.nome}:")
            avatar.utero.atualizar_tamanho_por_idade()
            avatar.utero.menstruar()
            avatar.utero.verificar_status()
        self.salvar()

    def fazer_funcoes_pele(self):
        for avatar in self.listar_avatares():
            print(f"\nVeja os status da pele do avatar {avatar.nome}:")
            # o bioma do avatar decide se é sol, picadas ou frio
            avatar.bioma.aplicar_efeito_pele(avatar, avatar.pele.protecao)
        self.salvar()
