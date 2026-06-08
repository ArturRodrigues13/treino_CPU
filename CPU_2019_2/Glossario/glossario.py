import time
import re

inicio = time.perf_counter()

while True:

	n = int(input())

	if(n == 0):
		break

	ultima = ""

	linha = input()
	linha = re.sub(r'[^a-zA-Z ]', ' ', linha)
	linha = linha.split()

	for x in range(n - 1):
		n_lin = input()
		n_lin = re.sub(r'[^a-zA-Z ]', ' ', n_lin)
		n_lin = n_lin.split()
		linha += n_lin

	linha.sort()

	for x in range(len(linha)):
		if(linha[x] != ultima):
			ultima = linha[x]
			print(linha[x])

	print()

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
