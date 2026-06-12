"""
    Verifica se um número é primo de forma otimizada.
"""
def e_primo(x):

    if x == 1:
        return False
    if x in (2, 3, 5, 7):
        return True
    if x % 2 == 0:
        return False

    # Busca até a raiz quadrada de x pulando os números pares
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

def mdc(a, b):

    x = max(a, b)
    y = min(a, b)
    resto = x % y
    while resto != 0:
        x = y
        y = resto
        resto = x % y
    return y

def mmc(a, b):

    return (a * b) // mdc(a, b)

def fatorial(n):

    if n <= 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def permutacao(n):
    """
    Permutação de N: Formas de alterar os elementos de uma sequência única.
    """
    return fatorial(n)

def arranjo(n, p):
    """
    Arranjo de n elementos dispostos p a p (cada elemento é único e a ordem importa)
    """
    return fatorial(n) // fatorial(n - p)

def combinacao(n, p):
    """
    Combinação de n tomados p a p: Escolhas não ordenadas (a ordem não importa).
    """
    return arranjo(n, p) // fatorial(p)

def permutacao_com_repeticao(n, repeticoes):
    """
    Permutação onde alguns elementos não são únicos (repetem r vezes).
    repeticoes: lista com a quantidade de vezes que cada item se repete.
    """
    numerador = fatorial(n)
    denominador = 1
    for r in repeticoes:
        denominador *= fatorial(r)
    return numerador // denominador

def permutacao_circular(n):
    """
    Permutação circular: Sequência disposta em círculo (ex: mesa redonda).
    """
    return fatorial(n - 1)

def arranjo_com_repeticao(n, p):
    """
    Arranjo onde de n elementos, podemos escolher p, podendo repetir o mesmo elemento.
    """
    return n ** p
