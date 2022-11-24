'''
Estruturas lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not
Operadores binários:
    - and, or, is
    
Regras de funcionamento:

para o 'and', ambos valores precisam ser True
para o 'or' um ou outro valor precisa ser True
para o 'not' o valor booleano é invertido, ou seja, se for True, vira False, se for False vira True
para o 'is', o valor é comparado com um segundo
'''

ativo = True
logado = True
if ativo and logado:
    print('Bem vindo usuario!')
else:
    print('Voce precisa ativar sua conta. Por favor, cheque seu e-mail')

ativo = True
logado = True
if not ativo:
    print('Voce precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem vindo usuario!')

print(ativo is True)
