## Programação com Acesso a Banco de Dados
# Revisão de Orientação a Objetos
# Prof. Guilherme Leal Santos

# Aula 19/09 - Orientação a Objetos
from conta import Conta
from cliente import Cliente

cliente1 = Cliente('Stray Kids', '123.456.789-10')

conta1 = Conta('Stray Kids', 1, 143, 'straykids@gmail.com', 123456789)
print(conta1)

conta1.extrato()
conta1.deposita(100)
conta1.extrato()

conta2 = conta1
conta2.extrato()
conta2.saca(100)
conta2.extrato()
conta1.extrato()

if(conta1.transfere(30) == False):
    print('Tá liso!')
else:
    print('OK!')





# Aula 26/09 - Listas e Funções de Alta Ordem

""" print('Bem vindos!')    

frutas = ['Maça', 'Banana','Laranja']
print(frutas)
print(frutas[0])
print(f'Tamanho: {len(frutas)}')

# Inserir ao final da lista:
frutas.append('Uva')
print(frutas)

# Inserir em uma posição específica:
frutas.insert(1,'Abacaxi')
print(frutas)

# Remove o último item da lista e retorna o valor removido:
fruta = frutas.pop(0) # Remove o elemento do índice 0
print(f'Removido: {fruta}')
print(frutas)

frutas.remove('Uva') # Remove o elemento com o valor 'Uva'
print(frutas)

numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(numeros)

# Ordenar - decrescente
numeros_ord_d = sorted(numeros, reverse=True)
print (f'Lista ordenada (decrescente): {numeros_ord_d}')

numeros_dobrados = []
for n in numeros:
    numeros_dobrados.append(n*2)
print(numeros_dobrados)

numeros_dobrados = list(map(lambda n: n*2, numeros))
print(numeros_dobrados)

numeros_filtrados = list(filter(lambda n: n > 4, numeros))
print(numeros_filtrados)

# calcular a soma dos números:
from functools import reduce

soma = reduce(lambda soma, n: soma + n, numeros)
print(soma) """




