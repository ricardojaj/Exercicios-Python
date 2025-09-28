#Exercicio 1 - Contador
#Crie uma função que peça um número N e conte de 1 até N.

def contador():
    try:
        numero = int(input("Digite um numero inteiro: "))
        i = 1
        for i in range(i, numero + 1):
            print(i)

    except ValueError:
        print("Numero digitado é invalido!")


contador()