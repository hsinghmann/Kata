import sys
x = 20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5
arr = str(x)
for line in x:
    number = line.split(",")
    odd = 0
    for i in range(len(number)):
        # print(number[i])
        odd = odd ^ int(number[i])
    print odd
