# Função para verificar se uma aresta pode ser colocada na árvore
def union(pais, rank, o, d):

	# Pega as "raízes" dos dois conjuntos que os vértices pertencem
	ro = find(pais, o)
	rd = find(pais, d)

	# Se tá no mesmo conjunto, ciclo, False
	if ro == rd:
		return False

	# Se não tá, ajusta o rank (evita ficar com uma árvore muito profunda e deixa a busca mais fácil)
	if rank[ro] < rank[rd]:
		pais[ro] = rd
	elif rank[ro] > rank[rd]:
		pais[rd] = ro
	else:
		pais[rd] = ro
		rank[ro] += 1

	return True

# Função pra encontrar a raiz
def find(pais, x):

	# Procura a raiz de forma recursiva enquanto atualiza a árvore, tornando as buscas ainda mais rápidas
	if pais[x] != x:
		pais[x] = find(pais, pais[x])
	return pais[x]
