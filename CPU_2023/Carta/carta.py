import time
import string

inicio = time.perf_counter()

tipo = input()
linha = input()
nova_linha = ""
vect = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def fibo(val:int):

	vetordobem = [1, 1] + [0] * (val - 1)

	for x in range(2, val + 1, 1):

		vetordobem[x] = vetordobem[x - 1] + vetordobem[x - 2]

	return vetordobem[val]

if(tipo == "C"):
	for x in range(len(linha)):
		letra = linha[x]
		if(letra not in string.ascii_lowercase):
			nova_linha = nova_linha + letra
			continue

		index = vect.index(letra) + 1
		fib = fibo(x)
		new_index = (index + fib) % 26
		nova_linha = nova_linha + vect[new_index - 1]

else:
	for x in range(len(linha)):
		letra = linha[x]
		if(letra not in string.ascii_lowercase):
			nova_linha = nova_linha + letra
			continue

		index = vect.index(letra) + 1
		fib = fibo(x)
		new_index = (index - fib) % 26
		nova_linha = nova_linha + vect[new_index - 1]

print(nova_linha)

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
