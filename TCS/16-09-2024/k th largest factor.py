#Kth largest factor of N:
n,k=map(int,input().split(','))
factors=[1,]
c=0
for i in range(2,(n//2)+1):
    if n%i==0:
        c+=1
        factors.append(i)
factors.append(n)
if c<k:
    print('1')
else:
    print(factors[-k])