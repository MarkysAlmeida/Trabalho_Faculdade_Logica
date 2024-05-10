print('      Bem-vindo a Loja de Gelados do Marcos      ')
print('-------------------Cardáprio---------------------')
print('-' * 49)
print('---| Tamanho  |  Cupuaçu (CP) |  Açai (AC)  | ---')
print('---|    P     |   R$  9.00    |   R$ 11.00  | ---')
print('---|    M     |   R$ 14.00    |   R$ 16.00  | ---')
print('---|    G     |   R$ 18.00    |   R$ 20.00  | ---')
print('-' * 49)

valor_pedido = 0
valor = 0

while True:
    # COLETANDO O DADO DO SABOR DO PEDIDO
    sabor = input('Entre com o SABOR desejado (CP/AC):').lower()

    # VERIFICANDO SE O QUE O USUARIO DIGITOU CORRESPONDE A OPÇÕES DISPONIVEL
    if sabor == 'cp':
        while True:
        #CASO A OPÇÃO SEJA VERDADEIRA, NO CASO CP (CUPUAÇU), CONTINUA O CODIGO
            tamanho = input('Entre com o TAMANHO desejado (P/M/G): ').lower()
            # COLETANDO O DADO DO TAMANHO DO PRODUTO QUE ELE VAI QUERER
            if tamanho == 'p':
                # SE ESCOLHEU A OPÇÃO P, VAI MOSTRAR NA TELA O VALOR E ACRESCENTAR O NÚMERO 9 A VARIAVEL VALOR
                print("Você pediu um CUPUAÇU no tamanho P: R$9,00")
                valor = 9
                break
            elif tamanho == 'm':
                # SE ESCOLHEU A OPÇÃO M, VAI MOSTRAR NA TELA O VALOR E ACRESCENTAR O NÚMERO 14 A VARIAVEL VALOR
                print("Você pediu um CUPUAÇU no tamanho M: R$14,00")
                valor = 14
                break
            elif tamanho == 'g':
                # SE ESCOLHEU A OPÇÃO G, VAI MOSTRAR NA TELA O VALOR E ACRESCENTAR O NÚMERO 18 A VARIAVEL VALOR
                print("Você pediu um CUPUAÇU no tamanho G: R$18,00")
                valor = 18
                break
            else:
                print('TAMANH0 inválido. Tente Novamente') #CASO DIGITAR OUTRA COISA QUE NÃO SEJA A OPÇÃO DEMONSTRADA
    elif sabor == 'ac':
        while True: #CASO A OPÇÃO SEJA VERDADEIRA, NO CASO AC (AÇAI), CONTINUA O CODIGO
            tamanho = input('Entre com o TAMANHO desejado (P/M/G): ').lower()
            # COLETANDO O DADO DO TAMANHO DO PRODUTO QUE ELE VAI QUERER
            if tamanho == 'p':
                # SE ESCOLHEU A OPÇÃO P, VAI MOSTRAR NA TELA O VALOR E ACRESCENTAR O NÚMERO 11 A VARIAVEL VALOR
                print("Você pediu um AÇAI no tamanho P: R$11,00")
                valor = 11
                break
            elif tamanho == 'm':
                # SE ESCOLHEU A OPÇÃO M, VAI MOSTRAR NA TELA O VALOR E ACRESCENTAR O NÚMERO 68 A VARIAVEL VALOR
                print("Você pediu um AÇAI no tamanho M: R$16,00")
                valor = 16
                break
            elif tamanho == 'g':
                # SE ESCOLHEU A OPÇÃO G, VAI MOSTRAR NA TELA O VALOR E ACRESCENTAR O NÚMERO 20 A VARIAVEL VALOR
                print("Você pediu um AÇAI no tamanho G: R$20,00")
                valor = 20
                break
            else:
                print('TAMANHO inválido. Tente Novamente') #CASO DIGITAR OUTRA COISA QUE NÃO SEJA A OPÇÃO DEMONSTRADA
    else:
        print('SABOR Inválido. Tente novamente') #CASO DIGITAR OUTRA COISA QUE NÃO SEJA A OPÇÃO DEMONSTRADA
    if sabor != 'cp' and sabor != 'ac':
    # TESTANDO QUE SE O CLIENTE DIGITOU ALGUMA COISA QUE NÃO SEJA AS OPÇões AC OU CP, VOLTA AO CODIGO SOLICITANDO
    # O SABOR QUE ELE QUER
        continue
    else:
        # CASO ELE JÁ DIGITOU TUDO CERTO E ESCOLHEU O SABOR
        valor_pedido = valor_pedido + valor # ATRIBUI O VALOR DA VARIAVEL SABOR E FAZ A SOMA
        c = input('Deseja mais alguma coisa ? (S/N):').lower()
        #CASO O CLIENTE DIGITE S
        if c == 's':
            continue  #VOLTA AO COMEÇO DO CODIGO SOLICITANDO O SABOR
        elif c == 'n':
        #CASO ESCOLHEU A OPÇÃO N
            print(f'O valor total a ser pago: R${valor_pedido:.2f}') # MOSTRA O QUANTO FICOU E ENCERRA O PROGRAMA
            break
        else:
            #CASO DIGITOU ALGO DIFERENTE, MOSTRA QUE DIGITOU ALGO DIFERENTE, ALÉM DO PREÇO A SER PAGO E ENCERRA O PROGRAMA
            print('Opção Inválida! Você digitou errado e entendemos que não deseja continua!')
            print(f'O valor total a ser pago: R${valor_pedido:.2f}')
            break
