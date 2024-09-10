n=int(input())
l=[str(x) for x in input().split()]
l=l+l
s=""
s=s.join(l)
s=int(s,2)
c=0
while(s!=0):
    s=(s & (s << 1))
    c+=1
print(c)