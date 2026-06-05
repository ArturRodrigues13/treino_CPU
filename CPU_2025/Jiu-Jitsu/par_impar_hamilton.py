while True:

	n = int(input())
	n *= 2
	if(n == 0):
		break

	tabela = [[0 for y in range(n) ] for x in range(n)]

	vetor = [1 if int(item) % 2 == 0 else 0 for item in input().split()]

	for x in range(1, n, 1):
		for i in range(n - x):
			j = x + i
			if(x%2):
				esc = vetor[i]
				dir = vetor[j]

				tabela[i][j] = tabela[i + 1][j] + esc if tabela[i + 1][j] + esc > tabela[i][j - 1] + dir else tabela[i][j - 1] + dir

			else:
				tabela[i][j] = tabela[i + 1][j] if tabela[i + 1][j] < tabela[i][j - 1] else tabela[i][j - 1]

	print(tabela[0][n - 1])
