list = [1,2,3,4]
res = []
dup=[]
dup_count=0
for i in list:
    if i in res:
        dup.append(i)
    else:
        res.append(i)
        print("no dup")
        break
print(f"Duplicate numbers are {dup}")
