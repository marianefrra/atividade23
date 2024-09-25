# Crie um programa que receba um número do usuário e exiba a tabuada desse número de 1 a 10.

def exibir_tab():
    numero = int(input("digite um número para exibir sua tabuada:"))
    print(f"tabuada de {numero}:")

    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} * {i} = {resultado}")

exibir_tab()