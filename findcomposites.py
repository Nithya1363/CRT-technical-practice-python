def isComposite(n):
    for i in range(2,(n//2)+1):
        if n%i == 0:
            return True
    return False
for i in [9,31,32,14,17,43,58,4,6]:
    if isComposite(i) == True:
        print(i)