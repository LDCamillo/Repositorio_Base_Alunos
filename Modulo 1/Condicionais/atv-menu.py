#FAZER UM MENU
#O MENU VAI FICAR EM LOOP
#ATÉ A PESSOA ESCOLHER A OPCAO 

def soma():
    n1 = float(input("digite o primeiro numero: "))
    n2 = float(input("digite o segundo numero: "))
    print(n1 + n2)

def subtração(n1,n2):
    print(n1,n2)

while True:
    opcao = input("1 - OPÇÃO 1\n2 - OPÇÃO 2\n0 - SAIR\n")


    if opcao == "1":
        soma()


    elif opcao == "2":
        numero1 = float(input("digite o primeiro numero: "))
        numero2 = float(input("digite o segundo numero: "))
        subtração(numero1,numero2)

    elif opcao == "0":
        print("Encerrando")
        break


    else:
        print("Opção inválida.")