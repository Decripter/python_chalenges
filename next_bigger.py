def next_bigger(n):
    if len(str(n)) > 1:
        num = str(n)
        arr = []
        bigger=num
        y =0
        temp = 0
        tempA=[]
        for x in range(0, len(num)):
            arr.append(num[x])

        lenar=len(arr)-1
        while y < lenar or int(bigger) < int(num) :

            if arr[lenar - y ] > arr[lenar - y -1 ]:
                

                tempA = arr[0:lenar-y-1]
                print(tempA)
                tempA += arr[y+1]
                tempA += arr[lenar-1-y]
                tempA += arr[lenar-y+1:len(arr)]

                arr = tempA    
                y += 1
            else:
                y += 1
            bigger =""
            for x in range(0, len(arr)):
                bigger = bigger + str(arr[x])
            if int(bigger) > int(num) :
                    y = lenar+1
            
        if bigger == num:
            bigger = -1    
        return int(bigger)
    else:
        return -1
#1404
#3210
#print(next_bigger(2252333))
print(next_bigger(2017))


# arr[1 2 3 3]
#     0 1 2 3

#  arr[1 2 3    3 ]
#      0 1 2    3

#  arr[1 2 3    3 ]
#      0 1 2    3
#x = 3

#3-len  = 3
#4-len  = 1

#temp arr = [x-3]
#append temp = [x-4]
#append resto[]