arr = [2,2,4,2,8,6,7]
counter = {}
for i in arr:
    if i not in counter:
        counter[i] = arr.count(i)
max_repeated_cnt = max(counter.values())
for i in arr:
    if counter[i] == max_repeated_cnt:
        print(f"Mode of {arr} is {i}")
        break