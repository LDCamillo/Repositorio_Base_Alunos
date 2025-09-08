nome = input("digite o nome: ")
email = input("digite o e-mail: ")

arquivo = open("pessoa.txt", "a", encoding="utf-8")
arquivo.write(f"{nome} | {email} \n")
arquivo.close()