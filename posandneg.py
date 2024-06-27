arr = [9,-31,32,-14,17,-43,58,4,-6,0]
pos = list(filter(lambda x:x>0,arr))
neg = list(filter(lambda x:x<0,arr))
print(f"pos are {pos} : {len(pos)}")
print(f"neg are {neg} : {len(neg)}")