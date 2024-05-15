def escolha_servico():
    global preco
    while True:
        print('\nEntre com o tipo de serviço desejado') #Print dos valores
        print('DIG - Serviço de digitalização - R$1.10 por página')
        print('ICO - Serviço de Impressão Colorida - R$1.00 por página ')
        print('IPB - Serviço de Impressão Preto e Branco - R$0.40 por página')
        print('FOT - Serviço de Fotocópia - R$0.20 por página ')

        servico = input('\nADigite (DIG/ICO/IPB/FOT) Para escolher o serviço: ').lower() #Usuario entra com a opção do serviço
        if(servico == 'dig'):#Se for DIG, valor sera 1.10
            preco = 1.10
            return preco
        elif(servico == 'ico'):#Se for ICO, valor sera 1.00
            preco = 1.00
            return preco
        elif (servico == 'ipb'):#Se for IPB, valor sera 0.40
            preco = 0.40
            return preco
        elif (servico == 'fot'):#Se for FOT, valor sera 0.20
            preco = 0.20
            return preco
        else:
            print('\nEscolha inválida, entre com o tipo do serviço novamente!')
def num_pagina():
    global paginas
    paginas = 0
    while True: #enquanto verdadeiro
        try:
            paginas = int(input('Digite a quantidade de páginas: '))
            if(paginas >= 20000): #se a página for maior ou igual a 20.000
                print('\nNão aceitamos tantas páginas de uma vez.\n Por favor, entre com o número de páginas novamente\n')
                continue #continuar até o cliente digitar um valor menor que 20.000
            break
        except: #Verificar se o usuario digitou um número e não uma letra
            print('\nA quantidade de páginas precisa ser um número inteiro e não letras ou caracteres.\n')
            continue
    if(paginas >= 2000 and paginas < 20000):
        desconto = paginas * (25/100)
        paginas -= desconto #Da os 25% de desconto e volta quantas paginas serão realmente cobradas
    elif(paginas >= 200 and paginas < 2000):
        desconto = paginas * (20/100)
        paginas -= desconto #Da os 20% de desconto e volta quantas paginas serão realmente cobradas
    elif(paginas >= 20 and paginas < 200):
        desconto = paginas * (15/100)
        paginas -= desconto #Da os 15% de desconto e volta quantas paginas serão realmente cobradas
    else:
        paginas *= 1 #Quantidade menor que 20, não é dado desconto
    return int(paginas) #Retorna o valor


def servico_extra():
    global total, extra
    while True:
        print('Deseja adicionar algum serviço? ')  # Selecionando os serviços
        print('1 - Encadernação Simples - R$15,00')
        print('2 - Encadernação Capa Dura - R$40,00')
        print('0 - Não desejo mais nada')
        opcoes = input('Entre com o número de páginas: ')#Entrando com a opção
        if (opcoes == '1'): #Verifica se usuario digitou 1
            extra = 15
            total = (preco * paginas) + extra
            break
        elif (opcoes == '2'): #Verifica se usuario digitou 2
            extra = 40
            total = (preco * paginas) + extra
            break
        elif (opcoes == '0'):  #Verifica se usuario digitou 0
            extra = 0
            total = preco * paginas
            break
        else:
            print('\nEscolha inválida, entre somente com o número do serviço!(1 , 2 ou 0)\n')



#Programa Principal
#Mensagem de BOAS VINDAS
print('Bem Vindo a Copiadora do Marcos Antônio')

#ESCOLHA DOS SERVIÇOS
escolha_servico()

#VENDO QUANTAS PÁGINAS O CLIENTE QUER FAZER
num_pagina()

#VERIFICAÇÃO DE SERVIÇO EXTRAS
servico_extra()

#MOSTRANDO OS VALORES
print(f'\nTotal: R${total:.2f} (serviço: {preco:.2f} * páginas: {paginas:.0f} + extra: R${extra:.2f})')



