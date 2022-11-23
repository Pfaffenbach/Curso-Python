'''
Tipo Float
'''

# Errado do ponto de vista do float, é gerado uma tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo em ponto de vista do float
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
res = (int(valor))
print(res)
print(type(res))

# Podemos trabalhar com numeros complexos
num_complex = 5j
print(num_complex)
print(type(num_complex))
