def fact(n):
    res = 1
    for i in range(2,n+1):
        res*=i
    return res
#factorial of 5
#print(fact(5))

#sum of factorial from 1 to 10
'''res=0
for i in range(1,11):
    res+=fact(i)
print(res % (10**9)+7)'''

#sum of factorial from 2 to 20
res=0
for i in range(2,21,2):
    res+=fact(i)
print(res % (10**9)+7)