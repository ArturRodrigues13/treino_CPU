# Busca Profundidade
def busca_profundidade(grafo, no, buscado, visitados=None):

	# Começa vazio
	if visitados is None:
		visitados = set()

	# Se eu achei quem tava procurando, encerra
	if(no == buscado):
		return True

	# Pra cada vizinho
	for vizinho in grafo["no_atual"]:
		if vizinho not in visitados:
			visitados.add(vizinho)
			# Recursão
			if(busca_profundidade(grafo, vizinho, buscado, visitados)):
				return True

	return False
