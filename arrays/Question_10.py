'''def count(N, C):
    c_count = {}
    for color in C:
        c_count[color] = c_count.get(color, 0) + 1
    return sum(1 for count in c_count.values() if count == 1)
n = int(input())
c = list(map(int,input().split()))
result = count(n, c)
print(result)'''


n=int(input())
l={}
c=0
s=list(map(int,input().split()))[:n]
for i in s:
    if i not in l:
        l[i]=1
    else:
        l[i]+=1
for i in l.values():
    if i==1:
       c+=1
print(c)
