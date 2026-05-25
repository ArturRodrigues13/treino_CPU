import time

inicio = time.perf_counter()

linha = [float(item) for item in input().split()]

val1 = linha[1] / linha[0]
val2 = linha[3] / linha[2]

if(val1 < val2):
	print("primeiro")
elif(val1 > val2):
	print("segundo")
else:
	print("ambos")

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
