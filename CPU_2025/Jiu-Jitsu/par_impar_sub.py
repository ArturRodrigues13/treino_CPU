while True:

	n = int(input())
	n *= 2
	if(n == 0):
		break

	tabela = [[0] * n for _ in range(n)]
	total = 0
	vetor = [1 if int(item) % 2 == 0 else 0 for item in input().split()]

	for x in range(n):
		tabela[x][x] = vetor[x]

	for x in range(1, n, 1):
		for i in range(n - x):
			j = x + i
			esc = vetor[i]
			dir = vetor[j]

			pega_esc = esc - tabela[i + 1][j]
			pega_dir = dir - tabela[i][j - 1]

			tabela[i][j] = max(pega_esc, pega_dir)

	total = sum(vetor)
	print((tabela[0][n - 1] + total) // 2)
