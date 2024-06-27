arr = [2,1,4,10,8,6,7,9]
arr.sort()
mid = len(arr) // 2
if len(arr) % 2 ==0:
    print(f"Median of {arr} is {(arr[mid] + arr[mid-1])//2}")
else:
    print(f"Median of {arr} is {arr[mid]}")