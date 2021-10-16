
        


    def separaItens(input):
        conta = input
        total = 0
        divisao = 0
        resto = 0
        itens = []
        itensFora = []
        resto = 0

        inicio = 0 #inicio do string 
        fim = 0 #fim da string ate o espaco em branco
        for x in range(inicio, len(conta)):
            if input[x] == " ":
                fim = x
                itens.append(conta[inicio:fim])
                inicio = fim+1
        itens.append(conta[inicio:len(conta)])
        

        clientes = itens[0]
        totalItens = itens[1]
        total = 0
        itens= itens[2:len(itens)]
        

        for y in range(0, len(itens)):
            if itens[y].isdigit():    
                total=total+int(itens[y])
            
                
        for z in range(int(totalItens)*2, len(itens)):
            itensFora.append(itens[z])




        n=0
        for a in range(0, len(itens)-len(itensFora)):
            
            if n < len(itensFora) and itens[a] == itensFora[n]:
                resto = resto + int(itens[a+1])


                n+=1
                a=0

        divisao = total - resto
        divisao = divisao / int(clientes)
        divisao = round(divisao)
        return total, divisao, resto



    print(separaItens("3 5 janta 30 agua 35 vinho 70 sobremesa 60 cerveja 50 agua cerveja"))