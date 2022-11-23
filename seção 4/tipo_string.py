'''
Tipo String
Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples
- Estiver entre aspas duplas
- Estiver entre aspas simples triplas
- Estiver entre aspas duplas triplas
'''

nome = 'Geek University'
print(nome)
print(type(nome))

nome = 'Angelina Jolie'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

# Usando funções
nome = 'Geek University'
print(nome.upper())  # deixa tudo maiusculo

nome = 'Geek University'
print(nome.lower())  # Deixa tudo minusculo

nome = 'Geek University'
print(nome.split())  # Transforma em uma lista de strings

nome = 'Geek University'
print(nome[0:4])  # Slice de string
print(nome[5:15])  # Slice de string

print(nome.split()[0])
print(nome.split()[1])

# [::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta
print(nome[::-1])

print(nome.replace('G', 'P'))
