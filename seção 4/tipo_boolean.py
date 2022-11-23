'''
Tipo Boolean

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com letra inicial maiúscula
'''

ativo = True
print(ativo)
print(type(ativo))

'''
Operações Básicas:
'''

# Negação (not):
'''
Fazer a negação, se o valor booleano for verdadeiro o resultado será falso,
se for falso o resultado será verdadeiro. Ou seja, sempro o contrário.
'''
print(not ativo)

# Ou (or):
'''
É uma operação binária, ou seja, de dois valores. Ou um ou outro de ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
'''

logado = False
print(ativo or logado)

# E (and):
'''
Também é uma operação binária, ou seja, depende de dois valores. Ambos os
valores devem ser verdadeiros.

True and True -> True
True and False -> False
False and True -> False
False and False -> True
'''

print(True and True)
print(True and False)
print(False and True)
print(False and False)
