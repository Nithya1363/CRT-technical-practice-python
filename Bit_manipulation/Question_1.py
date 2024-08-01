n=int(input())
s=''
res=''
while n!=0:
    r=str(n%2)
    s+=r
    n//=2
s=s[::-1]
for i in range(len(s)):
    if s[i]=='0':
        res+='1'
    else:
        res+='0'
print(int(res,2))