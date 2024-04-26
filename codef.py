import numpy as np


for i in range(int(input())): #number of test cases
    maxx = 0
    rows = []
    for j in range(int(input())): #number of rows
        n = int(input()) #number of tickets per day
        if maxx < n:
            maxx = n  #setting the maximum number of tickets for a lottery

        rows.append([int(x) for x in input().split()])

    padded_rows = [np.pad(row, (0, maxx - len(row)), mode='constant') for row in rows]
    matrix = np.vstack(padded_rows)   #making the matrix

    mat = matrix.copy()

    found= []
    for i in range(len(matrix)):
        row = matrix[i]
        mat = np.delete(mat, 0, axis=0)
        f = False
        for ele in row:
            if ele!= 0 and (not np.isin(ele,mat)): #checking for ticket in new matrix
                print(ele)
                found.append(ele)
                f = True
                break
        if not f:
            break

    #output
    if len(found) == 0:
        print(-1)
    else:
        print(found)

        
        