# Aula sobre tipos de dados no Python

x = 1 

print("Valor da variavel: " + str(x))

print("Tipo da variavel " + str(type(x))) # Imprime o tipo de x

x = "Canal"

print("Valor da variavel: " + str(x))

print("Tipo da variavel " + str(type(x))) # Imprime o tipo de x

x = False 


print("Valor da variavel: " + str(x))

print("Tipo da variavel " + str(type(x))) # Imprime o tipo de x

x = 15.6

print("Valor da variavel: " + str(x))

print("Tipo da variavel " + str(type(x))) # Imprime o tipo de x

# Resumidamente variaveis em Python nao sao definidas e podem ser atribuidas a mais de um tipo

print("-----------------------------------------------------------")

print("Coleções: ")

print("Lista:")
x = ["Carro " , "Moto" , "Bicileta" , 1.5 , 3 , True] # list / array

#listas em python aceitam varios tipos
#listas sao mutaveis , sendo possivel alterar seu valor

print(x) # imprime a lista
print(x[0]) # imprime o indice

y = range(0,100) #cria uma lista de 0 a 100 posicoes 

print("Tuplas:")


x = ("Carro " , "Moto" , "Bicileta" , 1.5 , 3 , True) # list / array

# tuplas sao listas imutaveis uma vez criadas, seus elementos não podem ser modificados 
# (não é possível alterar, adicionar ou remover elementos). 
# Isso faz das tuplas uma boa escolha quando você deseja garantir que os 
# dados permaneçam constantes ao longo do tempo.


z = {#dicionario
    
    "canal" : "CBF Cursos",
    "curso" : "Curso de Python",
    "nome" : "Franco"

} 

print("Valor: " + z["canal"]) # retornar o valor da chave canal
print("Valor da variavel: " + str(x))

"""
O tipo set em Python é uma coleção não ordenada de elementos únicos, ou seja, ele não permite elementos duplicados. 
Um set é mutável (você pode adicionar e remover elementos), mas seus elementos devem ser imutáveis 
(como números, strings, ou tuplas).

Sets são úteis quando você quer garantir que não haja valores duplicados em uma coleção ou 
quando precisa realizar operações matemáticas de conjuntos, como interseção, união, diferença, etc

"""














