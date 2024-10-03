import random
# TIPOS NUMERICOS BASICOS NO PYTHON

numeroInteiro = 10
numeroFloat = 6.5
numeroComplexo = 1j

print("Valor da variavel: " + str(numeroInteiro) + " Tipo: " + str((type(numeroInteiro))))
print("Valor da variavel: " + str(numeroFloat) + " Tipo: "  + str(type(numeroFloat)))
print("Valor da variavel: " + str(numeroComplexo) + " Tipo: "  +str(type(numeroComplexo)))

# a funcao str serve para transformar em string pois o python nao consegue concatenar tipos diferentes


numeroAleatorio = random.randrange(0,100) #gera um numero entre 0 e 100

print("O numero aleatorio foi: " + str(numeroAleatorio))

vetorDeNumeros = [random.randrange(0,100),random.randrange(0,100),random.randrange(0,100)]

print(vetorDeNumeros)

