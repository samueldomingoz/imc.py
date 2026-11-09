nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura * altura)

if imc< 18.5:
    print(f"Olá, {nome} seu IMC é: {imc:.2f} e com isso, você está abaixo do peso")
elif imc <25:
    print(f"Olá, {nome} seu IMC é {imc:.2f} e com isso, você está com o peso normal")
elif imc <30:
    print (f"Olá, {nome} seu IMC é {imc:.2f} e com isso, você está com o sobrepeso")
else:
    print (f"Olá, {nome} seu IMC é {imc:.2f} e com isso, você está com o obesidade")
