import time

inicio = time.perf_counter()

while True:
	try:
		dif = input()
		total_linhas = []
		total_colunas = []

		if(dif == "F"):

			m = [[0] * 3 for _ in range(3)]

			total_linhas = [0] * 3
			total_colunas = [0] * 3

			for x in range(4):

				l, c, v = map(int, input().split())

				m[l][c] = v

				total_linhas[l] += v
				total_colunas[c] += v

		elif(dif == "M"):
			m = [[0] * 4 for _ in range(4)]

			total_linhas = [0] * 4
			total_colunas = [0] * 4

			for x in range(9):

				l, c, v = map(int, input().split())

				m[l][c] = v

				total_linhas[l] += v
				total_colunas[c] += v

		elif(dif == "D"):
			m = [[0] * 5 for _ in range(5)]

			total_linhas = [0] * 5
			total_colunas = [0] * 5

			for x in range(16):

				l, c, v = map(int, input().split())

				m[l][c] = v
				total_linhas[l] += v
				total_colunas[c] += v

		total_linhas.sort(reverse=True)
		total_colunas.sort(reverse=True)

		fim = False
		for i in range(len(total_linhas)):
			if(total_linhas[i] > total_colunas[i]):
				print(1, total_linhas[i], total_colunas[i])
				fim = True
				break
			elif(total_colunas[i] > total_linhas[i]):
				print(2, total_colunas[i], total_linhas[i])
				fim = True
				break

		if(fim == False):
			print("Houve empate em todas as possibilidades")

	except EOFError:
		break

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
