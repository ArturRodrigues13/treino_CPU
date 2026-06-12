# Maior Soma de uma Subsequência em uma lista de valores positivos que tem um certo limite
valores = list(map(int, input().split()))

l = 0
soma = 0
max_len = 0

for n in range("n_valores"):
	# Adiciono o valor na sequência
	soma += valores[n]

	# Se estourei o limite, vou subtraindo da esquerda pra direita até entrar no limite de novo
	while soma > "valor_max":
		soma -= valores[l]
		l += 1

	# Se essa sequência foi maior que a anteriormente registrada, salva
	max_len = max(max_len, n - l + 1)

# Nesse caso eu tô retornando o tamanho da sequência, mas pra adaptar pra entregar a soma é super tranquilo
print(max_len)
