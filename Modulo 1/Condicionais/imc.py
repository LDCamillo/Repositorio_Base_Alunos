try:
    nome = input("qual seu nome? ")
    peso = float(input("qual o seu peso? "))
    altura = float(input("qual é sua altura? "))

except ValueError:
    print("erro de valor")
    exit()
except TypeError:
    print("sigite apenas numero!")
    exit()

imc = peso / (altura * altura)

if imc <= 18.5:
   situação = "abaixo do peso"
elif imc <= 24.9:
    situação = "peso normal"
elif imc <= 29.9:
    situação = "sobre peso"
elif imc <= 34.9:
    situação = "obesidade grau I"
elif imc <= 39.9:
    situação = "obdesidade grau II"
else:
    situação = "obesidade grau III"

with open("peso.txt", "a", encoding="utf-8") as peso_arquivo:
    peso_arquivo.write(f"{nome} \n situação do pasciente: {situação} ")
    
    #altura 