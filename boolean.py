# variaveis boolean são aquelas que tem apenas dois valores , verdadeiro e falso

x = True
y = False

print(x)
print(y)

# operadores logicos 

# and ( os dois devem ser verdadeiro)
# or ( apenas um precisa ser verdadeiro)
# not ( negacao do atual)

print(x and y) # saida falso pois apenas um eh verdadeiro
print(x or y)  # sai verdadeiro pois um eh verdaderio
print(not x)  # sai falso

# Qualquer valor em Python pode ser convertido para bool usando a função bool(). 
# Seguem algumas regras de conversão:
# Valores como 0, None, '' (string vazia), 
# [] (lista vazia), () (tupla vazia) e {} (dicionário vazio) são considerados falsos.
# Quaisquer outros valores sao verdadeiro

print(bool(0))       # False
print(bool(42))      # True
print(bool(""))      # False
print(bool("Python")) # True

