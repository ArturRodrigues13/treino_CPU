# Dividir uma lista de valores em dois conjuntos de forma que a diferença seja mínima.

# Uau, fui pesquisar o algoritmo da mochila e isso aqui já resolve ele também, bem que eu tinha achado parecido quando tava executando no papel, super legal cara. Pra adaptar, só separar os pesos e os valores e mudar no if do loop, m[i - 1][j - p[i]] + p[i] isso aqui pra m[i - 1][j - p[i]] + v[i], sendo v o vetor que armazena os valores de cada item e p o vetor com os pesos.

n, *valores = map(int, input().split())

p = [0] + valores

total = sum(valores)

t = total // 2

# Fazendo a matriz
m = [[0] * (t + 1) for _ in range(n + 1)]

# Tá, essa aqui é muuuuito confusa, mas basicamente, ann, ele tá verificando qual a maior soma possível usando i elementos, então eu comço usando só o primeiro e vou aumentando
for i in range(1, n + 1):
	for j in range(1, t + 1):

		# Pego o valor da linha de cima
		m[i][j] = m[i - 1][j]

		# Se eu não estourar o limite
		if p[i] <= j:

			# Se a soma for maior, muda
			if m[i - 1][j - p[i]] + p[i] > m[i][j]:
				m[i][j] = m[i - 1][j - p[i]] + p[i]

# O valor do menor dos dois subconjuntos
melhor = m[n][t]

# Diferença entre os dois conjuntos que formamos
print(total - 2 * melhor)
