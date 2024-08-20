s1=input()
s2=input()
res=[]
res.append(set(s1).intersection(s2))
res.append(set(s1)-set(s2))
res.append(set(s2)-set(s1))
print(res)