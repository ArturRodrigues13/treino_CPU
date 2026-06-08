import time

inicio = time.perf_counter()

while True:
	try:

		aposta = int(input())

		ganho = 0

		a, b = map(int, input().split())

		c, d = map(int, input().split())

		if(a == c and b == d or a == d and b == c):
			ganho = aposta * 6

		elif(a + b == c + d):
			ganho = aposta * 3

		elif((a + b) % 2 == (c + d) % 2):
			ganho = -(aposta // 2)
		else:
			ganho = -aposta

		print(ganho)

	except EOFError:
		break

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
