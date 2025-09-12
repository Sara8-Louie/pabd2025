## Programação com Acesso a Banco de Dados
# Revisão de Orientação a Objetos
# Prof. Guilherme Leal Santos

print('Bem vindos!')    

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
print(soma)



