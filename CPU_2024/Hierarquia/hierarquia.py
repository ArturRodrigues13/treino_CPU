import time

inicio = time.perf_counter()

def buscaPais(empresa, no, lista=None):

	if lista is None:
		lista = []
		lista.insert(0, no)

	if no == 1:
		return lista

	lista.insert(0, empresa[no])

	return buscaPais(empresa, empresa[no], lista)

while True:
	try:

		empresa = [0, 0]

		quant = int(input())
		funcionarios = [int(item) for item in input().split(" ")]

		for x in range(quant - 1):
			empresa.append(funcionarios[x])

		questoes = int(input())

		for x in range(questoes):

			a, b = map(int, input().split(" "))

			lista1 = buscaPais(empresa, a)
			lista2 = buscaPais(empresa, b)

			tam = min(len(lista1), len(lista2))
			resposta = 1

			for y in range(tam):
				if(lista1[y] == lista2[y]):
					resposta = lista1[y]
				else:
					break

			print(resposta)

	except EOFError:
		break

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
