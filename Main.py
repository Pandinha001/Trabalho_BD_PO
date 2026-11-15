from database import Session
from Sistema import Sistema


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
    for i, b in enumerate(biomas):
        print(f"{i}) {b.nome} (id {b.id_bioma})")
    indice = ler_numero("Escolha o índice do bioma: ")
    if 0 <= indice < len(biomas):
        return biomas[indice]
    print("Índice inválido!")
    return None


session = Session()
sistema = Sistema(session)

print("Seja bem vindo(a) ao BioLógica! \n Escolha seu bioma, avatar, e viva uma aventura cheia de aprendizados!")

while True:
    play = input("Deseja dar play na rodada? (s/n) ")
    if play == 's':
        opcao = ler_numero("O que deseja fazer? \n1)Criar um bioma \n2)Criar um avatar \n3)Ver status do avatar "
                           "\n4)Ver status do bioma \n5)Fazer nada \n6)Alimentar \n7)Hidratar \n8)Proteger "
                           "\n9)Movimentar \n10)Sair\n")

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
                # pele e útero já são criados juntos dentro do avatar na classe Organismo

        elif opcao == 3:
            sistema.ver_status_saude()
            sistema.fazer_funcoes_utero()
            sistema.fazer_funcoes_pele()

        elif opcao == 4:
            sistema.exibir_dados()

        elif opcao == 5:
            avatar = escolher_avatar(sistema)
            if avatar:
                avatar.fazer_nada()
                sistema.salvar()

        elif opcao == 6:
            print("\n--- Menu de Comidas ---\n")
            print("1. Carne podre")
            print("2. Carne Crua")
            print("3. Carne Assada")
            escolha = ler_numero("Escolha o número da sua comida: ")
            avatar = escolher_avatar(sistema)
            if avatar:
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

        else:
            print("Opção inválida!")

    elif play == 'n':
        print("Ok, volte sempre!")
        break
    else:
        print("Opção inválida!")

session.close()
