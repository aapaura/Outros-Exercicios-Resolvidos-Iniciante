# exercicios DSA - Python fundamentos - Cap 2

# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela

lista2 = ["amanda", "mariana", "vilma", "gilberto", 590]
print(lista2)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string

a = ["amanda"]
p = ["paura"]
c = a + p
print(c)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla

tupla = (1, 2, 2, 3, 4, 4, 4, 5)
print(tupla.count(4))


# Exercício 5 - Crie um dicionário vazio e imprima na tela

dicionario = {}
print(dicionario)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela

dic2 = {'y1':2, 'y2':4, 'y3':6}
print(dic2)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela

dic2['y4'] = 8
print(dic2)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.

dic3 = {"a":[1,2], "b":3, "c":4}
print(dic3)


# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
tupla2 = (1, 2)
dic4 = {"x":4, "y":5}
lista3 = ["K", tupla2, dic4, 0.5]
print(lista3)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de dados é o profissional mais sexy do século XXI'
print(frase[0:18])

