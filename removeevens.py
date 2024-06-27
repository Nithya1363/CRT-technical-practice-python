'''import copy
a = [1,2,3,5,7,9,11]
b=copy.deepcopy(a)
for i in a:
    if i%2==0:
        a.remove(i)
print(b,a)'''


arr = [1,2,3,5,7,9,11]
isDeleted = False
for i in arr:
    if i%2==0:
        arr.pop(i)
        isDeleted = True
        break
if isDeleted == True:
    print('not same after removing')
else:
    print('same after removing')