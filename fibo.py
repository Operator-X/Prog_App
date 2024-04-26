import numpy as np
A = np.array([[1,1],[1,0]])

num = int(input("fibo num:"))

if num <= 1:
    print("fibonacci number:",num)

else:
    
    lists = {}
    num_bin = bin(num)[2:]
    first = 0
    B = np.identity(2)
    for i in range(len(num_bin)):
        if first == 0:
            lists["A0"] = A
        else:
            lists["A"+str(first)] = np.dot(lists["A"+str(first-1)],lists["A"+str(first-1)])
        first += 1
        print(lists)
        
        if num_bin[i] == "1":
            B = np.dot(B,lists["A"+str(i)])
            print(B)



    value = np.dot(B,np.array([[1],[0]]))[1]
    print(value)