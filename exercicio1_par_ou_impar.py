# Exercício 1 - Número Par ou Ímpar
# Crie uma função que receba um número e diga se ele é par ou ímpar.
# O programa deve repetir até o usuário digitar 0.


def verificaNumero(num):
    if num % 2 == 0:
        print("Numero é par!")
    else:
        print("Numero é impar!")

numero = 1
while numero != 0:
    try:
        numero = int(input("Digite um numero inteiro: "))
        verificaNumero(numero)
    except ValueError:
        print("Numero digitado é invalido!")
print("Programa encerrado!")
