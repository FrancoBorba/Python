nome = "Franco  Ribeiro Borba" #variavel String

print(nome) # uma string eh uma lista(array) de caracteres

print(nome[0]) # imprime a posicao do caracter
print(nome[0:6]) # imprime da posicao 0 ate a 5

string = "Python"
print(string[0:3])  # Saída: Pyt (caracteres do índice 0 ao 2)
print(string[:4])  # Saída: Pyth (caracteres do início até o índice 3)
print(string[2:])  # Saída: thon (caracteres do índice 2 até o final)

concatenada = "Hello" + " " + "World"
print(concatenada)  # Saída: Hello World


# String são imutaveis ou seja impossivel nome[0] = "K" , geraria um erro

print(len(nome)) # imprime o tamanho da string

print(nome.lower()) # transforma todos caracteres em minusculo
print(nome.upper()) # transforma todos os caracteres em maiusculo

print(nome.strip()) # retira todos os espacos

print(nome.split())



