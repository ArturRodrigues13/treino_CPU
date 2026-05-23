import time

inicio = time.perf_counter()

dicionario = {

	".-":"a",
	"-...":"b",
	"-.-.":"c",
	"-..":"d",
	".":"e",
	"..-.":"f",
	"--.":"g",
	"....":"h",
	"..":"i",
	".---":"j",
	"-.-":"k",
	".-..":"l",
	"--":"m",
	"-.":"n",
	"---":"o",
	".--.":"p",
	"--.-":"q",
	".-.":"r",
	"...":"s",
	"-":"t",
	"..-":"u",
	"...-":"v",
	".--":"w",
	"-..-":"x",
	"-.--":"y",
	"--..":"z",
	".----":"1",
	"..---":"2",
	"...--":"3",
	"....-":"4",
	".....":"5",
	"-....":"6",
	"--...":"7",
	"---..":"8",
	"----.":"9",
	"-----":"0",
	"/":" "
}

while True:
	try:
		traducao = ""
		codigo = input().split(" ")

		for x in range(len(codigo)):
			codigo[x] = dicionario.get(codigo[x])

		traducao = "".join(codigo)
		print(traducao)

	except EOFError:
		break

fim = time.perf_counter()

print(fim - inicio)
