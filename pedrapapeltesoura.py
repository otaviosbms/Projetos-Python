#decisão player

print('____PEDRA PAPEL OU TESOURA PYTHON____')
print('\n...................')

p1 = input('\nEscolha: pedra, papel ou tesoura?\n')

if p1 == 'pedra':
    print('voce escolheu:', p1)

if p1 == 'papel':
    print('voce escolheu:', p1)

if p1 == 'tesoura':
    print('voce escolheu:', p1)

while p1 != 'pedra' and p1 != 'papel' and p1 != 'tesoura' and p1 != 'Pedra' and p1 != 'Papel' and p1 != 'Tesoura':
    p1 = str(input("A sua escolha é inválida.\nEscolha outra opção:\n"))
    if p1 == 'pedra' or 'Pedra':
        print('\nvoce escolheu:', p1)
        break
    if p1 == 'papel' or 'Papel':
        print('\nvoce escolheu:', p1)
        break
    if p1 == 'tesoura' or 'Tesoura':
        print('\nvoce escolheu:', p1)
        break
print('\n...................')

#decisão pc

import random

escolhapc = random.randrange(1, 4)

if escolhapc == 1:
    print('\nO computador escolheu: pedra')
    
if escolhapc == 2:
    print('\nO computador escolheu: papel')
    
if escolhapc == 3:
    print('\nO computador escolheu: tesoura')

print('\n...................')

#resultados:

r = (p1, escolhapc)

while True:
    if r == ('pedra', 1) or r == ('Pedra', 1):
        print('\nEmpate')
        break
    if r == ('papel', 2) or r == ('Papel', 2):
        print('\nEmpate')
        break
    if r == ('tesoura', 3) or r == ('Tesoura', 3):
        print('\nEmpate')
        break
    if r == ('tesoura', 1) or r == ('Tesoura', 1):
        print('\nVoce perdeu!')
        break
    if r == ('pedra', 2) or r == ('Pedra', 2):
        print('\nVoce perdeu!')
        break
    if r == ('papel', 3) or r == ('Papel', 3):
        print('\nVoce perdeu!')
        break
    if r == ('papel', 1) or r == ('Papel', 1):
        print('\nVoce ganhou!')
        break
    if r == ('tesoura', 2) or r == ('Tesoura', 2):
        print('\nVoce ganhou!')
        break
    if r == ('pedra', 3) or r == ('Pedra', 3):
        print('\nVoce ganhou!')
        break


