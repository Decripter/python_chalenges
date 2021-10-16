import string
def is_pangram(inpt):
    isPangram = False
    inpt = inpt.lower()
    inpArr = []
    alfa = []
    for x in range(97, 123):
        alfa.append(x)
    for x in range(0, len(inpt)):
        inpArr.append(ord(inpt[x]))
    inpArr = sorted(inpArr)
    x=0
    while x+1 < len(inpArr):
       
        if inpArr[x] == inpArr[x+1] or inpArr[x] < 97:
            inpArr.pop(x)
            
        else:
            x += 1

    if alfa == inpArr:
        isPangram = True
    return isPangram

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))