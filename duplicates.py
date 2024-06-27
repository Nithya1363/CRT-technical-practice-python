list = [1,2,3,2,4,2,4]
#print(len(list) != len(set(list)))
validated = set()
res = []
for num in list:
    if num in validated and num not in res:
        res.append(num)
        #print("has duplicates")
        #break
    validated.add(num)
if len(res) != 0:
    print(res)
else:
    print("no duplicates")