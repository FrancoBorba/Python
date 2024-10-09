minha_lista = [1, 2, 3, 'Python', True] # listas em python podem ter tipos diferentes

print(minha_lista)

carros = ["Hrv" , "Creta" , "Fusca" , "Renegade" , "Porshe"] # listas sao indexadas

print(carros)
print("imprime valor do incide 0 " + carros[0])

print(carros[-3]) # se utilizar um indice negativo acessa do final da lista

carros.append("Ferrari") # Apendi adiciona itens no final da lista
carros.append("Aston Martin")

print(carros)

carros[2] = " Corolla"

print(carros)

carros.insert(0,"Virtus") # Insere indicando o indice a ser inserido
print(carros)

carros.remove("Creta") # remove 

carros.pop() # Remove o item do index passado , se não passar index remove o ultimo

print(carros)

# carros.clear() remove todos os elementos da lista