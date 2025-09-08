controle = 1

while controle <= 3:
  

    nome = input("nome do aluno: ")
    nota_1 = float(input("insira a primeira nota: "))
    nota_2 = float(input("insira a segunda nota: "))
    nota_3 = float(input("insira a terceira nota: "))

    resultado = nota_1 + nota_2 + nota_3
    media = resultado / 3

    print(" A media do aluno",nome, 'foi', media)

    controle = controle + 1 