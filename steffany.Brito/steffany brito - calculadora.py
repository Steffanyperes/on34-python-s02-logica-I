valor1=input("digite o valor da soma 1: ") #soma
valor2= input("digite o valor da soma 2: ")

valor1 = int(valor1)
valor2 = int(valor2)
soma= valor1 + valor2
print(soma)
def par_ou_impar(soma):
    if soma % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

print(par_ou_impar(soma))

valor3 = input("digite o valor a ser multiplicado 1 :")#multplicação
valor4= input("digite o valor a ser multiplicado 2 :")

valor3 = int(valor3)
valor4 = int(valor4)
multiplicação = valor3*valor4
print(multiplicação)

def par_ou_impar_multiplicação(multiplicação):
    if multiplicação % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

print(par_ou_impar_multiplicação(multiplicação))

valor5 = input("digite o valor a ser dividido 1 :")
valor6 = input("digite o valor a ser dividido 2 :")

valor5 = int(valor5)
valor6 = int(valor6)
divisão= valor5/valor6
print(divisão)

def par_ou_impar_divisão( divisão ):
    if divisão % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

print(par_ou_impar_divisão(divisão))

valor7= input("digite o valor da subtração 1 :")#subtração
valor8 = input ("digite o valor da subtração 2 :")

valor7 = int(valor7)
valor8 = int(valor8)
subtração = valor7-valor8
print(subtração)

def par_ou_impar_subtração(subtração):
    if subtração % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

print(par_ou_impar_subtração(subtração))

valor9= input("digite o valor da potencia 1 :")#subtração
valor10 = input ("digite o valor da potencia 2 :")

valor9 = int(valor9)#potencia
valor10 = int(valor10)
potencia = valor9 **valor10
print(potencia)

def par_ou_impar_potencia(potencia):
    if potencia % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

print(par_ou_impar_potencia(potencia))