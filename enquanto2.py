#Forma Condicional 01

'''
senha = 123    #inicializando a variavel

while senha != 1234:
    senha = int(input('Informe sua senha: '))

print ('Login realizado!')

'''

#Forma Condicionl 02

tentativas = 3
while True: 

    senha = input('Informe sua senha: ')
    if senha == 'aluno2' and tentativas > 0:
        print ('Login realizado!')

        break       #comando para encerrar o while
    if tentativas > 0:
        print ('Erro de credencial. Você tem mais', tentativas - 1, 'tenttivas.')
        tentativas -= 1     #diminui a quantidade de tentativas

    if tentativas  <= 0:
        print ('XXXXX  Erro de login  XXXXXX')
        break