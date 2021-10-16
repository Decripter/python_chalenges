def unique_in_order(uniq):
    inpArr = []


    for x in range(0, len(uniq)):
        inpArr.append(uniq[x])
    x=0
    while x+1 < len(inpArr):
        if inpArr[x] == inpArr[x+1]:
            inpArr.pop(x)            
        else:
            x += 1

    return inpArr

print(unique_in_order("AAAABBBCCDAABBB"))