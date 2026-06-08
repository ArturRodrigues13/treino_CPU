import time

inicio = time.perf_counter()

c, l = map(float, input().split())

area = c * l

if area <= 12:
	print("9.000 BTUs")
elif area <= 16:
	print("12.000 BTUs")
elif area <= 24:
	print("18.000 BTUs")
elif area <= 29:
	print("22.000 BTUs")
elif area <= 32:
	print("24.000 BTUs")
elif area <= 37:
	print("28.000 BTUs")
elif area <= 40:
	print("30.000 BTUs")
else:
	print("Ar-condicionado Industrial")

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
