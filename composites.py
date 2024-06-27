def composites(arr):
    res = []
    for n in arr:
        for i in range(2,(n//2)+1):
            if n%i == 0:
                res.append(n) #yield n 
                return res # break
arr = [19,23,17,9]
print(list(composites(arr))) # type: ignore