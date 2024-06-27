a,b=map(int,input('enter a,b values : ').split())
res=[]
for i in range(20,101):
    if i % a==0 and i % b==0:
        res.append(i)
print(res)