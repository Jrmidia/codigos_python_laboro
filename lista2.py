valor = [] #criando uma lista vazia

'''for item in range (10, 14):
valor.append(item)

print(valor)

#PREENCHENDO UMA LISTA COM DADOS DINAMICOS'''

valor2 = []

while True: #enquanto a condição for verdadeira
    num = int(input("Informe um numero qualquer ou ZERO para encerrar: "))

    if num == 0:
        break #encerra o sistema
    else: 
        valor2.append(num)

print("\n #PROGRAMA ENCERRADO# \n")
print("Os números escolhidos foram: ")
print (valor2)

while True:
    opcao = int(input("Deseja apagar os números da lista? [1]-SIM ou [2]-NÃO:"))

    if opcao == 1:
        valor2.pop()
        print(valor2)       
    
    elif opcao == 2: 
        break #encerra o sistema
    
print("\n #PROGRAMA ENCERRADO# \n")