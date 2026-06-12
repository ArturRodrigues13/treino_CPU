# Busca Largura do bem
def buscaLargura(lista:list, no:int, buscado:int):

	visitados = set()
	visitados.add(no)

	# Fila pra definir quem devemos buscar
	fila = [[no, 0]]

	# Enquanto a fila existe
	while len(fila) > 0:

		# pego o vertice e outro parâmetro qualquer, se tiver
		"v, dist" = fila.pop(0)

		# Se achou, encerra
		if("v" == buscado):
			if("v" == no):
				return - 1
			return "dist" - 1

		# Coloca todos os filhos na fila e marca como visitados
		for "x" in lista["v"]:
			if("x" not in visitados):
				visitados.add("x")
				fila.append(["x, dist + 1"])
	return -1
