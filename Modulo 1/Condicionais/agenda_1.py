agendas = []


while True:
    opçao = input("Programa de Agenda\n1 - Cadastrar pessoas\n2 - Listar pessoa\n3 - Excluir pessoa\n0 - Sair\n")
    if opçao == "0":
        print("Saindo do programa...")
        break
    elif opçao == "1":
        print() #Só para não dar erro
        nome = input("digite o nome que deseja adicionar: ")
        agendas.append, nome
    elif opçao == "2":
        print() #Só para não dar erro
    elif opçao == "3":
        print() #Só para não dar erro
    else:
        print("Opção inválida.")