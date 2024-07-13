#
s = "9654321768"
s1 = ""
c=0
for i in range(len(s)):
    if i%2==0:
       c = 9 - int(s[i])
       s1+=str(c)
    else:
        s1+=s[i]
print(s1)
