import time

inicio = time.perf_counter()

agenda = [0 for _ in range(72)]
tarefas_desc = []
cont = 0
espaco_maximo = 0

loop = int(input())

for x in range(loop):

	t, *desc = input().split(" ")

	if(t == "A"):
		tarefas_desc.append(desc)
		indice = tarefas_desc.index(desc) + 1

		dur, dia, ini = map(int, input().split(" "))

		dia -= 1

		espaco = 0

		for y in range(dia * 24 + ini, 72, 1):

			if(agenda[y] == 0):
				espaco += 1
			else:
				espaco = 0

			if(espaco == dur):
				agenda[y + 1 - espaco: y + 1] = [indice] * dur
				break

	elif(t == "C"):

		indice = tarefas_desc.index(desc) + 1

		for y in range(72):
			if(agenda[y] is indice):
				agenda[y] = 0

for x in range(72):

	if(agenda[x] == 0):
		cont += 1
		if(cont > espaco_maximo):
			espaco_maximo = cont
	else:
		if(cont > espaco_maximo):
			espaco_maximo = cont
		cont = 0

print(espaco_maximo)

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
