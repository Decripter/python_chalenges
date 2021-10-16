def done_or_not(board): #board[i][j]
    finish = True
    row0 = list(board[0])
    row1 = list(board[1])
    row2 = list(board[2])
    row3 = list(board[3])
    row4 = list(board[4])
    row5 = list(board[5])
    row6 = list(board[6])
    row7 = list(board[7])
    row8 = list(board[8])

    for y in range(0,len(board)):
        if 45 != (row0[y] + row1[y] + row2[y] + row3[y] + row4[y] + row5[y] + row6[y] + row7[y] + row8[y]):
            finish = False
        

    for x in range(0,len(board)): #check lines if is ok
        if 45 != sum(board[x]):
            finish = False
            print(45 == sum(board[x]))
    
    if sum(row0[0:3]) + sum(row1[0:3]) + sum(row2[0:3]) != 45: #first block line one
        finish = False
    if sum(row0[3:6]) + sum(row1[3:6]) + sum(row2[3:6]) != 45: #second block line one
        finish = False
    if sum(row0[6:9]) + sum(row1[6:9]) + sum(row2[6:9]) != 45: #third block line one
        finish = False
    
    if sum(row3[0:3]) + sum(row4[0:3]) + sum(row5[0:3]) != 45: #first block line two
        finish = False
    if sum(row3[3:6]) + sum(row4[3:6]) + sum(row5[3:6]) != 45: #second block line two
        finish = False
    if sum(row3[6:9]) + sum(row4[6:9]) + sum(row5[6:9]) != 45: #third line block two
        finish = False
    
    if sum(row6[0:3]) + sum(row7[0:3]) + sum(row8[0:3]) != 45: #first block line tree
        finish = False
    if sum(row6[3:6]) + sum(row7[3:6]) + sum(row8[3:6]) != 45: #second block line tree
        finish = False
    if sum(row6[6:9]) + sum(row7[6:9]) + sum(row8[6:9]) != 45: #third block line tree
        finish = False

    
    
    if finish == True:
        return 'Finished!'
    else:
        return 'Try again!'
    

certo =                 [[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]



errado =                [[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]
print(done_or_not(certo))
  

#                        1, 3, 2,     5, 7, 9,    4, 6, 8
#                        4, 9, 8,     2, 6, 1,    3, 7, 5
#                        7, 5, 6,     3, 8, 4,    2, 1, 9

#                        6, 4, 3,     1, 5, 8,    7, 9, 2
#                        5, 2, 1,     7, 9, 3,    8, 4, 6
#                        9, 8, 7,     4, 2, 6,    5, 3, 1

#                        2, 1, 4,     9, 3, 5,    6, 8, 7
#                        3, 6, 5,     8, 1, 7,    9, 2, 4
#                        8, 7, 9,     6, 4, 2,    1, 3, 5
                        

