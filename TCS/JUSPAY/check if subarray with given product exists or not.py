a=list(map(int,input().split()))
target=int(input())
flag=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if target==a[i]*a[j]:
            flag=1
if flag==1:
    print("YES")
else:
    print("NO")