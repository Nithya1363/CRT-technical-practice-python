n,k=map(int,input().split())
l=list(map(int,input().split()))
l=set(l)
c=0
for i in l:
    if i-3<=i<=i+3:
        c+=1
print(c)