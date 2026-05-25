import time

inicio = time.perf_counter()

def BuscaPais(familia, filho, lista=None):

	if lista is None:
		lista = []
		lista.insert(0, filho)

	if familia[filho - 1] == None:
		return lista

	lista.insert(0, familia[filho - 1])
	return BuscaPais(familia, familia[filho - 1], lista)

while True:

	certo = True
	p, l, c, d = map(int, input().split(" "))

	if(p == 0 and l == 0 and c == 0 and d == 0):
		break

	familia = [None for _ in range(p)]

	for x in range(l):
		a, b = map(int, input().split(" "))

		familia[b - 1] = a

	lista1 = BuscaPais(familia, c)
	lista2 = BuscaPais(familia, d)

	comum = list(set(lista1) & set(lista2))

	if(len(comum) > 0):

		grau = max(len(lista1), len(lista2))

		for x in range(min(len(lista1), len(lista2))):
			if(lista1[x] == lista2[x]):
				grau -= 1
			else:
				certo = False
				print(f"Primos de grau {grau}")
				break

	if(c in lista2):
		grau = len(lista2) - 1 - lista2.index(c)
		certo = False
		print(f"Ascendente/Descendente de grau {grau}")

	if(d in lista1):
		grau = len(lista1) - 1 - lista1.index(d)
		certo = False
		print(f"Ascendente/Descendente de grau {grau}")

	if(certo):
		print("Casal Certo")

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
