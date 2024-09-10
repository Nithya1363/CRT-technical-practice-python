n=int(input())
a=list(map(int,input().split()))
k=int(input())
target=int(input())
if n<k:
    print('no')
else:
    for i in range(n-k+1):
        res=0
        for j in range(i,i+k):
            res+=a[j]
        if res==target:
            print('yes')
            print(*a[i:i+k])
            break
    else:
        print('no')
    #Method 2
    r=sum(a[:k])
    if res==target:
        print('yes')
        print(*a[:k])
    else:
        for i in range(k,n):
            res+=a[i]-a[i-k]
            if res==target:
                print('yes')
                print(*a[i-k+1:i+1])
                break
        else:
            print('no')