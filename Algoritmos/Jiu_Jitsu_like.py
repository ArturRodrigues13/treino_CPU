# Um jogo em que eu e o adversário jogamos de forma ótima e só podemos pegar das pontas (sim, só pra esse caso, se for outra coisa vai ter que fazer uma bela adaptação)
tabela = [[0] * "n" for _ in range("n")]

# Marca a diagonal principal com 0 (e o valor da escolha, nesse problema especificamente ele pede, então tem que guardar)
for x in range("n"):
	tabela[x][x] = [0, x]

# Avança diagonal por diagonal
for x in range(1, "n"):
	for i in range("n" - x):
		j = i + x

		# j = coluna, direita, i = linha, esquerda

		# Se eu pegar o da esquerda, vou ter aquele valor mais o valor da esquerda
		esc = tabela[i + 1][j][0] + "competidores"[i]

		# Se eu pegar o da direita, vou ter aquele valor mais o valor da direita
		dir = tabela[i][j - 1][0] + "competidores"[j]

		# Minha jogada se X % 2 == 1, caso contrário é a vez dele
		if(x % 2):
			tabela[i][j] = [esc,i] if esc  > dir else [dir, j]
		else:

			# Ele pega o menor valor, me empurrando pro pior futuro
			tabela[i][j] = [tabela[i + 1][j][0],i] if tabela[i + 1][j][0] < tabela[i][j - 1][0] else [tabela[i][j - 1][0], j]

x = 0
i = 0
j = "n" - 1

# Isso aqui é pro caso de precisarmos reconstruir as escolhas de cada time
for _ in range("n" // 2):

	if(tabela[i][j][1] == i):
		"time_meu".append("competidores"[i])
		i += 1
	else:
		"time_meu".append("competidores"[j])
		j -= 1

	if(tabela[i][j][1] == i):
		"time_dele".append("competidores"[i])
		i += 1
	else:
		"time_dele".append("competidores"[j])
		j -= 1


# Esse é outro método possível, ao invés de simular minha jogada e do adversário, eu mudo a abordagem e penso (se eu pegar esquerda, perco o que tem na direita, e vice versa)
for x in range(1, "n"):
	for i in range("n" - x):
		j = x + i

		# O que eu expliquei cá em cima
		esc = "vetor"[i] - tabela[i + 1][j][0]
		dir = "vetor"[j] - tabela[i][j - 1][0]

		# Pego o maior valor, e isso vai ser feito tanto por mim quanto por meu adversário
		if(esc > dir):
			tabela[i][j] = [esc, i]
		else:
			tabela[i][j] = [dir, j]


# Os dois métodos conseguem responder esse problema, porém, as duas tabelas que eles formas (apesar de ambas conseguirem armazenar os indíces das escolhas) passam duas informações diferentes, o método Hamiltoniano me dá a pontuação máxima naquele ponto do jogo considerando um certo intervalo, e esse de subtração nos dá a diferença entre a minha pontuação e a do adversário em cada ponto (ou seja, pode armazenar valores negativos, o que significa que ele tem n pontos a mais que eu)
