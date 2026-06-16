#!/usr/bin/env bash

# Uso: ./run.sh <codigo> <dir_entrada> <dir_saida> [tempo_max_seg]
#
# Roda o código para cada arquivo do diretório de entrada,
# comparando a saída com o respectivo arquivo do diretório de saída.
# A execução para se:
#   - a saída for diferente da esperada (mostra o diff), ou
#   - o tempo de execução ultrapassar o limite (padrão: 1 segundo).

if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]; then
    echo "Uso: ./run.sh <codigo (.cpp ou .py)> <dir_entrada> <dir_saida> [tempo_max_seg]"
    exit 1
fi

codigo="$1"
dir_entrada="${2%/}"   # remove barra final, se houver
dir_saida="${3%/}"
tempo_max="${4:-1}"    # padrão: 1 segundo

# Define o comando de execução de acordo com a extensão do código
extensao="${codigo##*.}"

if [ "$extensao" = "cpp" ]; then
    echo "Compilando $codigo..."
    g++ -O2 -o /tmp/run_bin "$codigo" || exit 1
    cmd="/tmp/run_bin"
elif [ "$extensao" = "py" ]; then
    cmd="python3 $codigo"
else
    exit 1
fi

# Itera sobre os arquivos de entrada em ordem natural (file1, file2, ..., file10)
for arquivo in $(ls "$dir_entrada" | sort -V); do
    echo "$arquivo..."

    entrada="${dir_entrada}/${arquivo}"
    saida_esperada="${dir_saida}/${arquivo}"

    # Executa o codigo, salva a saída e mede o tempo real
    TIMEFORMAT='%R'
    tempo=$( { time $cmd < "$entrada" > /tmp/run_saida.txt; } 2>&1 )

    # Compara a saída com o esperado; para e mostra o diff se forem diferentes
    if ! diff /tmp/run_saida.txt "$saida_esperada" --strip-trailing-cr; then
        break
    fi

    # Compara o tempo usando awk (disponível em qualquer sistema Unix)
    if awk "BEGIN { exit !($tempo > $tempo_max) }"; then
        echo "Tempo limite excedido: ${tempo}s > ${tempo_max}s"
        break
    fi

    echo "OK (${tempo}s)"
done
