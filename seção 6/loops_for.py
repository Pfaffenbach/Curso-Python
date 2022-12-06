'''
Loop for

Loop -> estrutura de repetição
For -> uma dessas estruturas

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis
Exemplos de iteráveis:
- String
    nome = 'Erich'
- Lista
    lista = [1,2,3,4]
- Range
    numeros = range(1,10)
'''

nome = 'Erich'
lista = [1,2,3,4]
numeros = range(1,10)

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)
print('----------------')

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)
print('----------------')

# Exemplo de for 3 (Iterando sobre um range)
for numero in numeros:
    print(numero)
print('----------------')

'''
Enumerate:
((0,'E'),(1,'R'),(2,'I'),(3,'C'),(4,'H'))

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)
OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline
'''
for i, v in enumerate(nome):
    print(nome[i])
print('----------------')

qtd = int(input("Quatas vezes deve rodar?"))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor:'))
    soma = soma + num
print(f'A soma é {soma}')
print('----------------')

'''
# Print sem pular linha
for letra in nome:
    print(letra, end='')
'''

# Tabela de emojis unicode: https://apps.timwhitlock.info/emoji/tables/unicode
# Original: U+1F60F
# Modificado: U0001F60F
for numero in range(1,4):
    for num in range(1,11):
        print('\U0001F60F'*num)
print('----------------')