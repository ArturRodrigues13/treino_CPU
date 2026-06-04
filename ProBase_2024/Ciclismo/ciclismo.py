import time

inicio = time.perf_counter()

c, l = map(int, input().split())

matrix_o = [[0 for _ in range(c)] for _ in range(l + 2)]

matrix_t = [[10000 for _ in range(c)] for _a in range(l + 1)]

matrix_t.insert(0,[0] * c)

for x in range(1, l + 1, 1):
	valor = [int(item) for item in input().split()]
	matrix_o[x] = valor

for x in range(1, l + 2, 1):
	for y in range(c):
		if(y != 0):
			resul = abs (matrix_o[x][y] - matrix_o[x-1][y-1]) + matrix_t[x-1][y-1]
			if(matrix_t[x][y] > resul):
				matrix_t[x][y] = resul

		resul = abs (matrix_o[x][y] - matrix_o[x-1][y]) + matrix_t[x-1][y]
		if(matrix_t[x][y] > resul):
			matrix_t[x][y] = resul

		if(y != c - 1):
			resul = abs (matrix_o[x][y] - matrix_o[x-1][y+1]) + matrix_t[x-1][y+1]
			if(matrix_t[x][y] > resul):
				matrix_t[x][y] = resul

print(min(matrix_t[l + 1]))

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
