def isPrime(n):
    for i in range(2,(n//2)+1):
        if n%i == 0:
            return False
    return True
for i in [2,3,4,12,13]:
    if isPrime(i) == True:
        print(i)