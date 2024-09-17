"""def ps(n):

    return 
n=int(input())
f=[1,]
for i in range(2,(n//2)+1):
    if n%i==0:
        f.append(i)
f.append(n)
print(f)
psl=[]
for i in range(1,len(f)):
    x=ps(i)
    if x==1:
        psl.append(i)
print(psl)
a=set(f)
b=set(psl)
c=a-b
print(c)
b,c=list(b),list(c)
count=0
for i in c:
    flag=1
    for j in range(1,len(b)):
        if i%b[j]==0:
            flag=0
            break
    if flag==1:
        count+=1
print(count)"""
n=int(input())
x=n**0.5
if x==int(x):
    print('yes')
else:
    print('no')