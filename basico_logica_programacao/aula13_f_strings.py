nome = 'Juliana Andrade'
altura = 1.62
peso = 69
imc = peso / (altura ** 2)

# f-strings = formatação de strings
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é {imc:.2f}'

print(linha_1)
print(linha_2)
