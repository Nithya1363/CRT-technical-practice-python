def swap(n,wor):
    c=0
    if len(n)!=len(wor):
        return c
    for i in range(len(n)):
        if n[i]!=wor[i]:
            c+=1
    return c
n=list(map(str,input().split()))
wor =input()
for i in range(len(n)):
    if (swap(n[i],wor)==2):
        n.append('True')
    else:
        n.append('False')
print(n)