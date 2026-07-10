print("=== AS RUÍNAS DE ELDORIA ===")

# Nome do usuário
nome = input("Digite seu nome:")

# Player
vida = 100
ouro = 10
karma = 0
print(f"Bem-Vindo, {nome}!")
print()
print(f"Vida: {vida}")
print(f"Ouro: {ouro}")
print(f"karma: {karma}")
print()
# Quest
print("O que deseja fazer?")
print()
print("1 - Explorar a floresta")
print("2 - Visitar a cidade")
print()

#Consequências
escolha = input("Escolha: ")
if escolha == "1":
# floresta
    print("Você entra na floresta e ouve um som estranho entre as árvores...")
    print('')
    print("1 - Investigar o barulho.")
    print("2 - Perguntar se há alguem lá.")
    escolha_floresta = input("Escolha: ")
    if escolha_floresta == "1":
        print("Um goblin sai de dentro do arbusto e com sua adaga desfere um golpe leve na sua perna")
        vida -= 15
        print(f"Você perdeu 15 de vida.")
        print(f"Vida restante: {vida}")
    elif escolha_floresta == "2":
        print("Um anão com cogumelo na cabeça e uma barba longa, talvez a mais linda já vista nesse bosque, aparece. Ele puxa o casaco e lhe dá 20 ouros")
        ouro +=20
        print(f"Agora, {nome} possui {ouro} ouro.")
    else:
        print("comando inválido")
# Cidade
elif escolha == "2":
    print("Enquanto caminhava a caminho da cidade você vê de longe uma carruagem...")
    print("Qual sua decisão?")
    print("1 - Pedir carona.")
    print("2- Roubar a carruagem.")
    escolha_cidade = input("Escolha: ")
    if escolha_cidade == "1":
        print(f"*{nome} corre até a carruagem*\n e para sua sorte você encontra um mercador gentil.\n * {nome} pede carona*.")
        print(f"O mercador aceita levando assim {nome} à cidade de Pontaris(cidade dos arcos)")
        print(f"*{nome}Chegou a Pontaris")
    elif escolha_cidade == "2":
        print(f"*{nome}Corre até a carruagem e sem pensar 2x derruba o Mercador gentil de cima da carruagem\n rouba seu dinheiro e foge para cidade*")
        print(f"""Após esse ato de crueldade, sem remorso... você foge com apenas os xingamentos fúteis do mercador.
        {nome}: ganhou +30 ouros
        {nome}: acumulou +70 de karma   
""")
        ouro += 30
        karma += 70
        print(f"""===Status atual===
        Vida: {vida}
        Ouro: {ouro}
        Karma: {karma}
        
        A aventura continua na cidade...
""")
    else:
        print("Comando inválido")

else:
    print("Comando inválido")





