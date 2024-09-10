s=input()
res=""
j=0
for i in s:
    if i in 'aeiouAEIOU':
        res+=str(j%10)
        j+=1
    else:
        res+=i
print(res)