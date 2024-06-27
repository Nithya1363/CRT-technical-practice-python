import copy
arr1 = [2,3,4,5]
arr2 = copy.deepcopy(arr1)
arr1.append(10)
print(arr1,arr2)