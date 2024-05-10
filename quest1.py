print('Bem Vindo a loja do Marcos Antônio')
# Recolhimento dos dados
valorUnit = float(input('Digite o valor do produto: R$'))
quantidade = int(input('Digite a quantidade de produto(s): '))

#Soma dos dados
soma = valorUnit * quantidade

# Se Valor for IGUAL OU MAIOR que 2500 e MENOR QUE 6000 aplicar desconto de 4%;
if (soma >= 2500 and soma < 6000):
    desconto = soma * (4 / 100)
    valorDesc = soma - desconto
    print(f'O valor SEM desconto: R${soma}')
    print(f'O valor COM desconto: R${valorDesc} (4% de DESCONTO)')

# Se Valor for IGUAL OU MAIOR que 6000 e MENOR QUE 10.000 aplicar desconto de 7%;
elif (soma >= 6000 and soma < 10000):
    desconto = soma * (7 / 100)
    valorDesc = soma - desconto
    print(f'O valor SEM desconto: R${soma}')
    print(f'O valor COM desconto: R${valorDesc} (7% de DESCONTO)')

# Se Valor for IGUAL OU MAIOR que 10.000 aplicar desconto de 11%;
elif (soma >= 10000):
    desconto = soma * (11 / 100)
    valorDesc = soma - desconto
    print(f'O valor SEM desconto: R${soma}')
    print(f'O valor COM desconto: R${valorDesc} (11% de DESCONTO)')
else:
# Como o valor foi menor que 2500 o desconto foi de 0% logo não há necessidade de calculo
    print(f'Valor da compra: R${soma}, (0% de DESCONTO)')
    print(f'GASTE MAIS DE R$2500.00 PARA RECEBER UM DESCONTO')