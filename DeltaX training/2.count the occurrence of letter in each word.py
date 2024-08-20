def countL(s,w):
    res=[]
    for i in s:
        res.append(i.count(w))
    return res
s=input().lower().split()
w=input().lower()
print(countL(s,w))