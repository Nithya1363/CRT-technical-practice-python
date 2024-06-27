data = [
    # name age salary id
    ("Teja",22,15000,517),
    ("Lav",25,10000,506),
    ("Nithya",21,50000,510),
    ("Keerthi",30,30000,521)
]
data.sort()
print(data)#sort data descending
data.sort(key = lambda x:x[1])
print(data)# sort data ascending
data.sort(key = lambda x:x[1],reverse = True)
print(data)#
print(max(data,key = lambda x:x[1])[0])
print(min(data,key = lambda x:x[1])[0])
print(max(data,key = lambda x:x[2])[0])