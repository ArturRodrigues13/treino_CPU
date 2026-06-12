# De início, a distância pra todos os pontos é infinito, pois não sabemos qual é ainda
distancias = {i: float('inf') for i in range("n")}

# A distância para o próprio ponto é 0
distancias["ponto inicial"] = 0

# Verificar se não teve nenhuma mudança, aí podemos acabar o algoritmo mais cedo
mudanca = False

# Loop roda no máximo n-1 vezes
for x in range("n_vertices" - 1):

	mudanca = False

	# Itera sobre cada vertice
	for y in range("n_vertices"):

		# Se o vertice já foi atingido
		if distancias["no_atual"] != float('inf'):

			# Pra cada nó vizinho, verificamos a distância e atualizamos se for menor que a registrada
			for vizinho, dist in "grafo"["no_atual"]:
				caminho = "dist_atual" + "dist"

				# Se for menor, atualiza, e definine que uma mudança ocorreu
				if caminho < distancias[vizinho]:
					distancias[vizinho] = caminho
					mudanca = True

	# Se não ocorreu mudança, todas as distâncias já foram registradas e o algoritmo pode parar mais cedo
	if(mudanca == False):
		break




# Outra versão, iterando apenas sobre as arestas, se for mais interessante armazenar dessa forma para uma questão específica
for _ in range("n_vertices" - 1):

	mudanca = False

    # Percorrer todas as arestas
	for o, d, peso in "grafo":

        # Relaxar só se o nó de origem já foi descoberto
		if distancias[o] != float('inf'):
			caminho = distancias[o] + peso

            # Se achou um caminho menor, atualiza
			if caminho < distancias[d]:
				distancias[d] = caminho

	if(mudanca == False):
		break
