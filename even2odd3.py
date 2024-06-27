res=0
for i in range(1,21):
    if i%2==0:
        res+=i**2
    else:
        res+=i**3
print(res)