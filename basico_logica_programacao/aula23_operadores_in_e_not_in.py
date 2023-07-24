# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6
#  A n d r a d e
# -6-5-4-3-2-1-0
# nome = 'Andrade'
# print(nome[2])
# print(nome[-4])
# print('rade' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('ade' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')