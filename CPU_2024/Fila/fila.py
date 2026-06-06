import time

inicio = time.perf_counter()

class Pessoa:
	def __init__(self, id:int, tipo:str):
		self.id = id
		self.tipo = tipo

while True:
	n = int(input())
	if(n == 0):
		break

	fila = []
	id_atual = 0

	for x in range(n):
		linha = input().split()

		if(linha[0] == "E"):
			id_atual += 1
			tipo = linha[1]
			p: Pessoa = Pessoa(id_atual, tipo)
			if(tipo == "C"):
				fila.append(p)

			else:
				tam = len(fila)

				if(tam == 0):
					fila.append(p)

				else:

					try:
						ind = 0
						for c in fila:
							if(c.tipo == "C"):
								break
							ind += 1

						p_seg = 0
						inserido = False

						for y in range(ind + 1, tam):

							if(fila[y].tipo == "C" and p_seg < 3):
								fila.insert(y, p)
								inserido = True
								break
							elif(fila[y].tipo == "P"):
								p_seg += 1
							elif(fila[y].tipo == "C"):
								p_seg = 0

						if(not inserido):
							fila.append(p)
					except:
						fila.append(p)

		else:
			print(fila[0].id, end=" ")
			fila.pop(0)

	for pessoa in fila:
		print(pessoa.id, end=" ")
	print()

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
