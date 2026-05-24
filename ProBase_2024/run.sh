script="$1"
prefixo_entrada="$2"
prefixo_saida="$3"

for arquivo in ${prefixo_entrada}*; do
    echo Rodando $arquivo
    python "$script" < "${arquivo}" | diff - "${prefixo_saida}${arquivo/#$prefixo_entrada}" --strip-trailing-cr
done
