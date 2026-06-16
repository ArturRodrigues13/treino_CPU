while True:
	c, k, t = input().split()

	if(c == "0" and k == "0" and t == "0"):
		break

	c = int(c)
	k = int(k)

	if(t == "D"):
		v = 2
	elif(t == "T"):
		v = 3
	else:
		v = 1

	vetor = [[x + 1, v] for x in range(c)]

	ind = k - 1


	while len(vetor) > 1:
		if(ind > len(vetor) - 1):
			ind = (ind % len(vetor))

		if(vetor[ind][1] == 1):
			vetor.pop(ind)

		else:
			vetor[ind][1] -= 1

		ind += k - 1

	print(vetor[0][0])
