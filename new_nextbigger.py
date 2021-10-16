def next_bigger(n):

	arrNumber = []
	inicio = []
	menor = []
	maior = []
	fim = []
	new = []
	final=""



	for x in str(n):
		arrNumber.append(x)

	for a in range(0, len(arrNumber)):
		

		if arrNumber[len(arrNumber)-a-1] > arrNumber[len(arrNumber)-a-2]:
			
			if a+1 - len(arrNumber) == 0:
				inicio = []
				resto = arrNumber[len(arrNumber)-a+1 : len(arrNumber)]
			else:

				inicio = arrNumber[0:len(arrNumber)-a-2]
				resto = arrNumber[len(arrNumber)-a : len(arrNumber)]
			
			maior = [int(arrNumber[len(arrNumber)-a-1])]
			menor = [int(arrNumber[len(arrNumber)-a-2])]
			

			new = inicio+maior+menor+resto

			break
		else:
			new = arrNumber
	
	x = 0
	while x < len(new):
		final = final+str(new[x])
		
		x+=1
	final = int(final)

	if int(final) == int(n) or int(final) < int(n):
		return int(-1)
	else:
		return final
	







test = 5391
cont = 5913	   
print(test)
print(next_bigger(test))
print(cont)
a=next_bigger(test)
print(next_bigger(a))
print(cont < next_bigger(test) and cont > test)



