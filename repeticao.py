'''for usado para quando se sabe quantos passos serão repetidos

for(etapa1; etapa2; etapa3){

}'''

#range exclui o valor final da contagem, ignora o ultimo valor da contagem

#EXEMPLO 01
for contador in range(1, 11):
    print (contador, end=', ')
    print('\n')

#EXEMPLO 02
for contador in range (10,-1, -2):
    print (contador, end=', ')
    print('---')

#EXEMPLO 03
for contador in range(0, 20, 2):
    print(contador, end=', ')
    print('---')