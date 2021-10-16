
def potenciar(num, base):
    num=int(num)
    potencia=0
    calc = 0 
    potencia = num
    for x in range(base-1):
        potencia = potencia * num
    return(potencia)

def narcissistic(num):
    base = 0
    narc = False
    while narc == False and base <10:
        num = str(num)
        temp = 0
        result = 0
        for a in range(0, len(num)):        
            result = (potenciar(num[a], base))
            temp = temp + result
        narc = str(num) == str(temp)
        base += 1
        print(base)
    return str(num) == str(temp) 








print(narcissistic(7))
