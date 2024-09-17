n=int(input())
a,b=0,1
while n:
    c=a+b
    a,b=b,c
    n-=1
print(c)