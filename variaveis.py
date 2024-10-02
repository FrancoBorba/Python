num1 = num2 = res = 0 #sao variaveis globais e podem ser acessadas por qualquer funcao
canal = "CBF cursos" # escopo global

def cn(): # esta eh uma funcao (estudaremos depois)
    print(canal)

cn()    

def canal():
    canalEscopoLocal = "CBF curso" # esta variavel so pode ser acessada dentro do escopo da funcao
    # global variavel ; tambem eh possivel criar uma variavel como global dentro de um escopo
    # se deve atribuir o valor apos a quebra de linha quando se declara como global
    global teste
    teste = "teste"
    print(canalEscopoLocal)

canal()

print(canal) # nao da erro
#print(canalEscopoGlobal)
print(teste)
 