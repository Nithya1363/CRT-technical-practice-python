#
s = input()
d = {}
res=""
count=0
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1
for i in d:
    res = res+i+str(d[i])
print(res)
