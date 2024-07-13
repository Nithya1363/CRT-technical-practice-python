s = input()
s=s.replace('-','')
n=10
res=0
for i in s:
    if i=='X':
        res+=10
    else:
        res+=int(i)*n
    n-=1
if res%11==0:
    print("Valid")
else:
    print("Invalid")