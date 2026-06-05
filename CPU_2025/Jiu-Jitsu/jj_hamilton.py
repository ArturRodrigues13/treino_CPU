import time

inicio = time.perf_counter()

while True:

	try:

		n, *competidores = [int(item) for item in input().split()]
		time_dele = []
		time_meu = []

		tabela = [[0] * n for _ in range(n)]

		for x in range(n):
			tabela[x][x] = [0, x]

		for x in range(1, n):
			for i in range(n - x):
				j = i + x

				esc = tabela[i + 1][j][0] + competidores[i]
				dir = tabela[i][j - 1][0] + competidores[j]

				if(x % 2):
					tabela[i][j] = [esc,i] if esc  > dir else [dir, j]
				else:
					tabela[i][j] = [tabela[i + 1][j][0],i] if tabela[i + 1][j][0] < tabela[i][j - 1][0] else [tabela[i][j - 1][0], j]

		x = 0
		i = 0
		j = n - 1

		for _ in range(n // 2):

			if(tabela[i][j][1] == i):
				time_meu.append(competidores[i])
				i += 1
			else:
				time_meu.append(competidores[j])
				j -= 1

			if(tabela[i][j][1] == i):
				time_dele.append(competidores[i])
				i += 1
			else:
				time_dele.append(competidores[j])
				j -= 1

		time_meu.sort(reverse=True)
		time_dele.sort(reverse=True)

		vitorias = 0
		i = 0
		j = 0

		while(i < len(time_meu) and j < len(time_dele)):
			if(time_meu[i] > time_dele[j]):
				i +=1
				j +=1
				vitorias +=1
			else:
				j += 1

		print(vitorias)

	except EOFError:
		break

fim = time.perf_counter()

tempo = fim - inicio


print(tempo)
