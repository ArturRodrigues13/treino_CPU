# Super algoritmo do mal eba

# Bom ressaltar, por mais que eu ainda ache muito confuso, pra dividir entre os dois conjuntos, depois de fazer toda a execução do algoritmo, você faz mais uma busca, ainda só visitando quem tem fluxo > 0. Quem você conseguiu chegar = grupo S, quem não conseguiu = grupo T. Disso, tu olha pro grafo original, todo mundo que vai de S pra T é o nosso corte mínimo, as arestas que estão limitando nossa rede. Legal guys iupi eba

# Buscando o primeiro caminho aumentante disponível (caminho aumentante se refere a uma caminho qualquer que ainda podemos passar fluxo)
def BFS(grafo:list, origem:int, destino:int, pais:list):

	visitados = [False]*(destino + 1)

	fila = []

	fila.append(origem)
	visitados[origem] = True

	while fila:

		atual = fila.pop(0)

		# Pra cada esteira da máquina atual, se não visitamos um lugar ainda, vamos pra lá, se achamos o destino, retornamos true, e nosso vetor pais armazena o caminho que pegamos
		for ind, val in enumerate(grafo[atual]):
			if visitados[ind] == False and val > 0:
				fila.append(ind)
				visitados[ind] = True
				pais[ind] = atual
				if ind == destino:
					return True

	# Não achou nenhum caminho, cabou
	return False

def FordFulkerson(grafo:list, origem:int, destino:int):

	# Armazenar o caminho que utilizamos
	pais = [-1]*(destino + 1)

	fluxo_max = 0

	# Enquanto achar um caminho
	while BFS(grafo, origem, destino, pais) :

		# Encontra o máximo de fluxo que podemos passar nesse caminho
		fluxo_caminho = float("Inf")
		s = destino
		while(s !=  origem):
			fluxo_caminho = min (fluxo_caminho,grafo[pais[s]][s])
			s = pais[s]

		fluxo_max += fluxo_caminho

		# Volta a origem atualizando o grafo residual com as arestas reversas, permitindo desfazer envios de fluxo
		s = destino
		while(s !=  origem):
			u = pais[s]
			grafo[u][s] -= fluxo_caminho
			grafo[s][u] += fluxo_caminho
			s = pais[s]

	# Se não tem mais caminho aumentante, retorna o fluxo_max encontrado
	return fluxo_max


# Tá, nesse caso aqui v seriam as máquinas e a as esteiras, disso nós criamos a matriz vXv porque assim, nesse caso fica meio paia usar matriz de adjacência porque ficamos subtraindo e somando do fluxo e acho que assim fica melhor pra organizar
v, a = map(int, input().split(" "))

maq = [[0 for _ in range(v)] for _ in range(v)]

for x in range(a):
	o, d, f = map(int, input().split(" "))
	maq[o - 1][d - 1] = f

# Grafo residual, pois é legal manter o original inalterado
maq_c = maq.copy()
fluxo_max = FordFulkerson(maq_c, 0, v - 1)
print(fluxo_max)
