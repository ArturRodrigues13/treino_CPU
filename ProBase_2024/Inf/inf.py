import time

inicio = time.perf_counter()

while True:
	try:

		a, r, e, c = input().split(" ")

		a = float(a)
		r = float(r)
		e = int(e)
		c = int(c)

		erro_max = 10 ** -e
		resul_antigo = 0
		n = 1
		soma = 0

		while True:
			resul = a / r ** n
			soma += resul
			if resul <= erro_max:
				break

			n += 1
			resul_antigo = resul

		print(n, end=" ")
		print(f"{soma:.{c}f}")


	except EOFError:
		break

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
