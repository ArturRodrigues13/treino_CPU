import time

inicio = time.perf_counter()

while True:
    dias, m_val = map(int, input().split())

    if dias == 0 and m_val == 0:
        break

    valores = list(map(int, input().split()))

    l = 0
    soma = 0
    max_len = 0

    for d in range(dias):
        soma += valores[d]

        while soma > m_val:
            soma -= valores[l]
            l += 1

        max_len = max(max_len, d - l + 1)

    print(max_len)

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
