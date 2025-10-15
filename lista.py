#criando uma lista

num = [3, 5, 8, 10, 14]

#print(type(num))

print(num)

num[2] = 15  #alterando o valor

#rxibir todos os numeros

for item in num:
    print(item)

#inserindo valores na lista

num.append(23)

print(num)

#addicionando itens em qualquer indice da lista

num.insert(2, 90) #inserirndo o valor 90 no índice 2 - ele cria um novo índice e empurra os demais 

print(num)

#removendo item da lista

num.pop() #remove o ultimo item da lista / colocando um numero ele remove o indice correspondente
print(num)