#inputting the value of the exponential
n = int(input("enter the value of exponential:"))

#conversion into binary and looking a binary part
bina = bin(n)[2:]

#number of ones
ones = bina.count("1")

#len of binary
l = len(bina)

#total number of multiplications
num = ones + l -1

print("the total number of multiplications are :",num)
