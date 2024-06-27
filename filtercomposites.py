def composite(arr):
    res = []
    for n in arr:
        for i in range(2,(n//2)+1):
            if n%i == 0:
                yield n 
                break
res = list(composite([9,31,32,14,17,43,58,4,6]))
print(list(filter((lambda x:x>=10 and x<=20),res)))