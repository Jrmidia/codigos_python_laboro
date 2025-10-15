frutas = ("Banana", "Uva", "Morango", "Acerola")

#print(type(frutas))


frutas[2] = 'Manga' #aqui da erro, a tupla é imutável, ou seja, não aceita mudança em tempo de execução

print(frutas)


for item in frutas:
    print(item[1])