

	

def processInput ( input ):
    "Aqui você deve criar seu algoritmo para processar a entrada e depois retorna-la."
    C=input

    F=list(range(0, 101))

    print(F)
    i=0
    while i < C:
        F.append(F[0]) 
        F.pop(0)
        i+=1
	
    
    

    return F[0]
print(processInput(2))