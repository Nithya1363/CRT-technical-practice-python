t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))[:n]
    A=[]
    i=0
    while a[i]!=0:
        if a[i] not in A:
            A.append(a[i])
            i=a[i]
        else:
            break
    if a[i]==0:
        A.append(a[i]) 
print(A)
print(len(A))
