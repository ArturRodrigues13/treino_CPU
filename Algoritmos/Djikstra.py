import heapq

# De início, a distância pra todos os pontos é infinito, pois não sabemos qual é ainda
distancias = {i: float('inf') for i in range("n")}

# A distância para o próprio ponto é 0
distancias["ponto inicial"] = 0
fila_prioridade = [(0, "ponto inicial")]

while fila_prioridade:

	# Pega o elemento no topo da pilha
	"dist_atual", "no_atual" = heapq.heappop(fila_prioridade)

	# Se é maior do que a que registramos anteriormente, descarta
	if "dist_atual" > distancias["no_atual"]:
		continue

	# Pra cada nó vizinho, verificamos a distância e atualizamos se for menor que a registrada
	for vizinho, dist in "grafo"["no_atual"]:
		caminho = "dist_atual" + "dist"

		# Se for menor, atualiza
		if caminho < distancias[vizinho]:
			distancias[vizinho] = caminho
			heapq.heappush(fila_prioridade, (caminho, vizinho))

# Isso aqui é só uma das formas legais que podemos pegar a distância de pontos específicos
valores = {ilha: custo for ilha, custo in distancias.items() if ilha in "destino"}

# Gostei muito disso
menor = min(valores, key=valores.get)
