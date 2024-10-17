# Primeira condicional if
# O if(se ) verifica se uma condicao eh verdadeira , se for executa os comandos do bloco

num1 = 5
num2 = 10

a = True

b = False

if a:  # sintaxe do if
    print("Condição verdadeira")

if num1 > num2:
    print("Não sera executado")

if num2 > num1:
    print("Numero 10 maior do que 5")

if not b:
    print("A negação de b é verdade")


if (num1 + num2) == 15:
    print("Resumindo qualquer retorno de boolean pode ser analisado pelo if")


num1 = 10
num2 = 20

if(num1 > num2) : # se for verdadeiro executa este bloco
    print("O numero " + str(num1) + " é maior do que :"  + str(num2))
else : # se nao for executa este
     print("O numero " + str(num2) + " é maior do que :" + str(num1))

a = 10

if(a >= 20):
    a = a - 10
elif( a >= 10):
    a = a - 5
else :
    a = a - 1

print("Valor de a após a execução : " + str(a))




    

