import time

inicio = time.perf_counter()

while True:
	try:
		n, *valores = map(int, input().split())

		p = [0] + valores

		total = sum(valores)

		t = total // 2

		m = [[0] * (t + 1) for _ in range(n + 1)]

		for i in range(1, n + 1):
			for j in range(1, t + 1):

				m[i][j] = m[i - 1][j]

				if p[i] <= j:
					if m[i - 1][j - p[i]] + p[i] > m[i][j]:
						m[i][j] = m[i - 1][j - p[i]] + p[i]

		melhor = m[n][t]

		print(total - 2 * melhor)

	except EOFError:
		break

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
