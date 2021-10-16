def divideArray(input):
	num = []
	tempA = []
	tempB = []
	y=0
	input = str(input)
	for x in range(0, len(str(input))):
		num.append(input[x])

	print(num)

	while y < len(num)-1:

					
		
		if num[len(num)-y-1] > num[len(num)-y-2]:
			print(str(num[len(num)-y-1])+" é maior que "+str(num[len(num)-y-2]))
			print(num[y])
			print(num[0:y])
			print(num[y:len(num)])
			tempA = 0
			y += 1
		else:
			y+=1


divideArray(1233)

#pegar menor numero e mover para direita