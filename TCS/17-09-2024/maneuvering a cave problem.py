def  cave(a,b):
    if a==1 or b==1:
        return 1
    else:
        return cave(a-1,b)+cave(a,b-1)
t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    x=cave(m,n)
    print(x)