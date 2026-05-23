import time

inicio = time.perf_counter()

casa = [int(item) for item in input().split(" ")]
gato = [int(item) for item in input().split(" ")]

if((gato[0] - casa[0])**2 + (gato[1] - casa[1])**2 <= casa[2]**2):
	print("Gato")
else:
	print("Gaiato")

fim = time.perf_counter()

print(fim - inicio)
