import math
num=int(input())
num2=1
li=[]
num3=1
while(num>1):  
    num2=num2*num
    num=num-1
    li.append(num)
for i in li:
    k=math.factorial(i)
    num3=num3*k
final=num3*num2
print(final)

