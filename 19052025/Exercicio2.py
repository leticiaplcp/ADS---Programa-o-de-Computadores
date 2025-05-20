def exibirMensagens(nome):
    print(f"Olá {nome}, tudo bem?")
    print("Estou no método")

for i in range(5):
    nome = input("Digite o seu nome: ")
    exibirMensagens(nome)
