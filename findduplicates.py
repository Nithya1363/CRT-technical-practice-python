list = [1,2,3,2,4]
res = []
dup=[]
dup_count=0
for i in list:
    if i in res:
        dup.append(i)
        dup_count+=1
    else:
        res.append(i)
print(f"list without duplicates are {res}\nDuplicate numbers are {dup}\nCount of duplicate numbers is {dup_count}")