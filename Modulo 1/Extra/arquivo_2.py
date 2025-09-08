nome = input("Digite o nome: ")
email = input("Digite o e-mail: ")

with open("pessoa.txt", "a") as arquivo:
    arquivo.write(nome + " | " + email + "\n")