'''
Saindo de loops com break

Utilizamos o break para sair de loops de maneira projetada
'''

# Exemplo 1
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('saiu do loop')
print('-----------------')

# Exemplo 2
while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break
print('saiu do loop')
print('-----------------')