'''
Ranges

- Precisamos conhecer o loop for para usar os ranges
- Precisamos conhecer o range para trabalhar melhor com loops for

Ranges são utilizados para gerar sequencias numéricas, não de forma aleatória,
mas sim de maneira especificada.

Formas Gerais:

#Forma 1
range(valor_de_parada)
OBS: valor_de_parada não inclusive (inicio padão 0, e passo 1 em 1)

#Forma 2
range(valor_de_inicio, valor_de_parada)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo 1 em 1)

#Forma 3
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuário)

#Forma 4 (Inverse)
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (valor_de_inicio especificado pelo usuário, e passo especificado pelo usuário)
'''

# Forma 1
for num in range(11):
    print(num)
print('-----------------------')
# Forma 2
for num in range(3,6):
    print(num)
print('-----------------------')
# Forma 3
for num in range(2,10,2):
    print(num)
print('-----------------------')
# Forma 4
for num in range(10,2,-2):
    print(num)