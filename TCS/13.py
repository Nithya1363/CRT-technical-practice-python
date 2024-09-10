n=int(input())
l=list(map(int,input().split()))
flag=True
for i in range(len(l)):
    if l[i]%2==0:
        l[i]=l[i]//2
    if l[i]%3==0:
        l[i]=l[i]//3
print(l)
for i in range(len(l)):
    if l[0]!=l[i]:
        flag=False
if flag==True:
    print("YES")
else:
    print("NO")

#Method-2
n=int(input())
arr=list(map(int,input().split()))
count=0
flag=0
for i in range(n):
    while arr[i]%2==0:
        arr[i]=arr[i]//2
    while arr[i]%3==0:
        arr[i]=arr[i]//3
    for i in range(1,n):
        if arr[i]==arr[0]:
            flag=1
        else:
            count+=1
    if flag!=0:
        print("NO")
    else:
        print("YES")
