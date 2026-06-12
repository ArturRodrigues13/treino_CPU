# Só coisinhas bobas que eu acho pertinente ter anotado :)

# um exemplo de uso de zip
""" boi.append(sum(x * p for (x, p) in zip(notas, pesos))) """

# Ordenação do bem
""" bois.sort(key=lambda x:(x[2],*[i for i in x[1]]),reverse=True) """

# Print do bem
""" print(*[nome[0] for nome in bois],sep="\n") """

# Lista de elementos que estão em duas listas ao mesmo tempo
""" comum = list(set(lista1) & set(lista2)) """

# Um exemplo de join sei lá
""" formata = ", ".join(str(num) for num in ganhadores) """

# Exemplo de Enumerate
""" indices = [i for i, valor in enumerate(datas) if valor >= consulta[0] and valor <= consulta[1]] """

# Outro print do bem
""" print(*[filmes[i] for i in indices], sep="\n") """

# Karaoke slop
""" dist_esc = valor_ori + 12.0 - valor_nov
	dist_dir = valor_nov - valor_ori """

# Bruh
""" print("".join(frase)) """

# Casa decimal vindo de variável

""" print(f"{soma:.{c}f}") """

# Whatever lil bro
""" procura = slop.find(caracteres[i],ini) """

# Vagas do mal

"""
	index = estacionamento.index(placa)
	estacionamento = estacionamento[index + 1:] + estacionamento[:index]
	estacionamento.append(espera.pop(0))
	print(" ".join(estacionamento),end="")
"""

# Pegar apenas certos caracteres, nesse caso, pega tudo que não for a-z, A-Z e " " e troca por " "
""" linha = re.sub(r'[^a-zA-Z ]', ' ', linha) """
