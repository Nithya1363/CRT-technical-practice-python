import math

def prime(a):
    flag=0
    for i in range(2,(a//2)+1):
        if a%i==0:
            flag=1
            break
    if flag==1 or a==1:
        return None
    else:
        return a

n=int(input())
a=list(map(int,input().split()))[:n]
m=min(a)
a.remove(m)
lcma=math.lcm(*a)
print(prime(lcma+m))