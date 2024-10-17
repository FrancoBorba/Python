# O loop for é usado para iterar sobre uma sequência (como listas, strings, tuplas,
# ou ranges de números).
# A cada iteração, ele atribui o próximo item da sequência a uma variável temporária.

frutas = ["maçã", "banana", "laranja" , "maracuja" , "tomate"]

for fruta in frutas:
    print(fruta)

# A função range() gera uma sequência de números, que pode ser usada em loops.
for i in range(5):  # range(5) gera números de 0 a 4
    print(i)


for i in range(2, 10, 2):  # Inicia em 2, vai até 10, com passo 2
    print(i)

# range(start, stop, step)

# O loop while repete um bloco de código enquanto uma condição é verdadeira.
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Incrementa a variável contador


 # O comando break é usado para interromper o loop prematuramente,
 #  mesmo que a condição do loop ainda seja verdadeira.
for i in range(10):
    if i == 5:
        break  # Para o loop quando i for igual a 5
    print(i)

 # O continue é usado para pular o restante do código no loop atual e passar para a próxima iteração.
for i in range(5):
    if i == 2:
        continue  # Pula o número 2
    print(i)







# looping infinito 
while True:
    print("Isso vai rodar para sempre!")

