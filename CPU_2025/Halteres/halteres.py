import time

inicio = time.perf_counter()

_, *valores_linha1 = [int(item) for item in input().split(" ")]
_, *valores_linha2 = [int(item) for item in input().split(" ")]

val1 = sum(valores_linha1)
val2 = sum(valores_linha2)

if(val1 == val2):
	print("OK")
elif(val1 > val2):
	val1 -= val2
	print(f"E > D: {val1} kg")
elif(val2 > val1):
	val2 -= val1
	print(f"E > D: {val2} kg")

fim = time.perf_counter()

print(fim - inicio)
