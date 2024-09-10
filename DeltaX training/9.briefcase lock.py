def lock(c,n):
    l1=list(map(int,c))
    l2=list(map(int,n))
    res=0
    for i in range(4):
        t=abs(l1[i]-l2[i])
    if t>5:
        res+=(10-t)
    else:
        res+=t
    return res
c=input()
n=input()
print(lock(c,n))