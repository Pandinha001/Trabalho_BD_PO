from database import Session
from Sistema import Sistema
import os
os.system('cls')


def ler_numero(mensagem, tipo=int):
    while True:
        try:
            return tipo(input(mensagem))
        except ValueError:
            print("Digite um número válido.")


def escolher_avatar(sistema):
    avatares = sistema.listar_avatares()
    if not avatares:
        print("Nenhum avatar criado ainda.")
        return None
    print("\n --- AVATARES ---")
    for i, a in enumerate(avatares):
        print(f"{i}) {a.nome} ({a.bioma.nome})")
    indice = ler_numero("Informe o índice do avatar: ")
    if 0 <= indice < len(avatares):
        return avatares[indice]
    print("Índice inválido!")
    return None


def escolher_bioma(sistema):
    biomas = sistema.listar_biomas()
    if not biomas:
        print("Nenhum bioma cadastrado. Crie um bioma primeiro (opção 1).")
        return None
    print("\n --- BIOMAS ---")
    for i, b in enumerate(biomas):
        print(f"{i}) {b.nome} (id {b.id_bioma})")
    indice = ler_numero("Escolha o índice do bioma: ")
    if 0 <= indice < len(biomas):
        return biomas[indice]
    print("Índice inválido!")
    return None


def montar_menu(tem_avatar):
    op = {1: "Criar um Bioma", 2: "Criar um Avatar", }
    if tem_avatar:
        op.update({
            3: "Ver status do avatar",
            4: "Ver status do bioma",
            5: "Fazer nada",
            6: "Alimentar",
            7: "Hidratar",
            8: "Proteger",
            9: "Movimentar",
        })
    op[10] = "Sair"
    return op


session = Session()
sistema = Sistema(session)

print("Seja bem vindo(a) ao BioLógica! \n Escolha seu bioma, avatar, e viva uma aventura cheia de aprendizados!")

while True:
    play = input("Deseja dar play na rodada? (s/n) ")
    if play == 's':
        opcao = montar_menu(len(sistema.listar_avatares()) > 0)
        print("\n O que deseja fazer? ")
        for numero, texto in opcao.items():
            print(f"{numero}: {texto}")
        opcao = ler_numero("")

        if opcao == 1:
            print("\n--- Biomas ---\n")
            print("1. Floresta Tropical")
            print("2. Savana")
            print("3. Tundra")
            escolha = ler_numero("Escolha o número do seu bioma: ")
            sistema.criar_bioma(escolha)

        elif opcao == 2:
            bioma = escolher_bioma(sistema)
            if bioma:
                nome = input("Dê um nome: ")
                idade = ler_numero("Informe a idade: ")
                peso = ler_numero("Informe o peso: ", float)
                sistema.criar_avatar(nome, idade, peso, bioma)
                print("Avatar criado com sucesso!")
       

        elif opcao == 3:
            avatar = escolher_avatar(Sistema)
            if avatar:
                sistema.ver_status_saude()
                sistema.fazer_funcoes_utero()
                sistema.fazer_funcoes_pele()

        elif opcao == 4:
            bioma = escolher_avatar(Sistema)
            if bioma:
                sistema.exibir_dados()

        elif opcao == 5:
            avatar = escolher_avatar(sistema)
            if avatar:
                avatar.fazer_nada()
                sistema.salvar()

        elif opcao == 6:
            avatar = escolher_avatar(sistema)
            if avatar:
                print("\n--- Menu de Comidas ---\n")
                print("1. Carne podre")
                print("2. Carne Crua")
                print("3. Carne Assada")
                escolha = ler_numero("Escolha o número da sua comida: ")
                avatar.alimentar(escolha)
                sistema.salvar()

        elif opcao == 7:
            print("\n--- Menu de Hidratação ---\n")
            print("1. Água Potável")
            print("2. Água de coco")
            print("3. Água suja")
            escolha = ler_numero("Escolha o número da sua hidratação: ")
            avatar = escolher_avatar(sistema)
            if avatar:
                avatar.hidratar(escolha)
                sistema.salvar()

        elif opcao == 8:
            print("\n--- Menu de Proteção para a Pele ---\n")
            print("1. Protetor Solar")
            print("2. Repelente")
            print("3. Blusa de frio")
            escolha = ler_numero("Escolha o número da sua proteção: ")
            avatar = escolher_avatar(sistema)
            if avatar:
                avatar.proteger(escolha)
                sistema.salvar()

        elif opcao == 9:
            avatar = escolher_avatar(sistema)
            if avatar:
                distancia = ler_numero("Informe a distância que você deseja movimentar o seu avatar: ", float)
                avatar.movimentar(distancia)
                sistema.salvar()

        elif opcao == 10:
            print("Ok, volte sempre!")
            break

        elif opcao 3 <= opcao <= 9:
            print("Opção inválida!")

        else:
            print("Opção inválida!")

    elif play == 'n':
        print("Ok, volte sempre!")
        break
    else:
        print("Opção inválida!")
        continue

session.close()
