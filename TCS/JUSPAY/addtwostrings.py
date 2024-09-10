from re import L


s=input()
t=input()
res=""
for i in range(len(s)):
    res+=s[i]+t[i]
if len(s)>len(t):
    res+=s[i+1:]
elif len(s)<len(t):
    res+=t[i+1:]
print(res)
