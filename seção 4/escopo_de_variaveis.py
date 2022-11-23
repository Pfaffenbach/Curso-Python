'''
Escopo de variaveis

Dois casos de escopo:
1- Variaveis globais;
    - Variaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.
2- Variaveis Locais
    - Variaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.
    
Python é uma linguagem de tipagem dinamica. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Esse tipo é inferido ao atribuirmos o valor a mesma.
'''

num = 6  # Exemplo de variável global
print(num)
print(type(num))

num = "Geek"
print(num)
print(type(num))

nao_existo = 'Oi'
print(nao_existo)

num = 6

if num > 5:
    novo = num + 4  # Variavel novo é uma variável local
    print(novo)
