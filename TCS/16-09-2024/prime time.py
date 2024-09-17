"""
1   13  25
2   14
3   15
4   16
5   17
6   18
7   19
8   20
9   21
10  22
11  23
12  24  36
"""
import math


def prime(a):
    if a==1:
        return 0
    for i in range(2,int(math.sqrt(a)+1)):
        if a%i==0:
            return 0
    return 1
d,p=map(int,input().split())
n=int(d//p)
c=0
for i in range(2,n):
    flag=1
    for j in range(p):
        num=i+j*n
        if not prime(num):
            flag=0
            break
    if flag:
        c+=1
print(c)