import time

inicio = time.perf_counter()

while True:

	try:

		n, *vetor = [int(item) for item in input().split()]

		tabela = [[0] * n for _ in range(n)]

		for i in range(n):
			tabela[i][i] = [vetor[i], 0]

		for x in range(1, n):
			for i in range(n - x):
				j = x + i
				esc = vetor[i] - tabela[i + 1][j][0]
				dir = vetor[j] - tabela[i][j - 1][0]

				if(esc > dir):
					tabela[i][j] = [esc, i]
				else:
					tabela[i][j] = [dir, j]

		i = 0
		j = n - 1
		meu = []
		seu = []
		lim = n // 2

		for _ in range(lim):

			if(tabela[i][j][1] == i):
				meu.append(vetor[i])
				i +=1
			else:
				meu.append(vetor[j])
				j -=1

			if(tabela[i][j][1] == i):
				seu.append(vetor[i])
				i +=1
			else:
				seu.append(vetor[j])
				j -=1

		meu.sort(reverse=True)
		seu.sort(reverse=True)

		i = 0
		j = 0
		u = 0

		while(j < lim and i < lim):
			if(meu[i] > seu[j]):
				i += 1
				j += 1
				u += 1
			else:
				j += 1

		print(u)

	except EOFError:
		break

fim = time.perf_counter()

print(fim - inicio)
