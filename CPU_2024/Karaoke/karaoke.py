import time

inicio = time.perf_counter()

tabela = {
	"C": 0.0,
	"D": 2.0,
	"E": 4.0,
	"F": 5.0,
	"G": 7.0,
	"A": 9.0,
	"B": 11.0
}

notas = int(input())

original = input().split()
novo = input().split()
soma = 0

for x in range(notas):
	valor_ori = tabela[original[x][0]]
	valor_nov = tabela[novo[x][0]]
	if(len(original[x]) > 1):
		if(original[x][1] == "#"):
			valor_ori += 1.0
			if(valor_ori == 12.0):
				valor_ori = 0.0
		else:
			valor_ori -= 1.0
			if(valor_ori == -1.0):
				valor_ori = 11.0

	if(len(novo[x]) > 1):
		if(novo[x][1] == "#"):
			valor_nov += 1.0
			if(valor_nov == 12.0):
				valor_nov = 0.0
		else:
			valor_nov -= 1.0
			if(valor_nov == -1.0):
				valor_nov = 11.0

	if(valor_ori < valor_nov):
		dist_esc = valor_ori + 12.0 - valor_nov
		dist_dir = valor_nov - valor_ori
	else:
		dist_esc = valor_nov + 12.0 - valor_ori
		dist_dir = valor_ori - valor_nov

	soma += min(dist_dir, dist_esc)

print(f"{soma / 2:.1f}")

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
