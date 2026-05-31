import time

inicio = time.perf_counter()

while True:

	flag = 0

	i, p = map(int, input().split(" "))

	if(i == 0 and p == 0):
		break

	mapa = [[] for _ in range(i)]

	for x in range(p):
		o, d = map(int, input().split(" "))

		mapa[o - 1].append(d)
		mapa[d - 1].append(o)

	for x in range(i):
		if(mapa[x] == []):
			flag = 1
			print("S")
			break

	if(flag == 0):
		print("N")

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
