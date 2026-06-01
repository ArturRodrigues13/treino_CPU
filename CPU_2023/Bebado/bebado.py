import time

inicio = time.perf_counter()

percentual = input().replace("%","")

percentual = float(percentual)

if(percentual > 0.06):
	print("FLAGRADO ALCOOLIZADO")
else:
	print("LIVRE")

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
