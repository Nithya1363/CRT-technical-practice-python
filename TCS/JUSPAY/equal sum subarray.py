"""Split an array into 2 equal sum subarrays
input: [1,2,3,4,5,5]
output: [1,2,3,4][5,5]
input: [4,3,2,1]
output: Not Possible"""
n=int(input())
a=list(map(int,input().split()))[:n]
leftsum=sum(a)
rightsum=0
for i in range(n-1,-1,-1):
    rightsum+=a[i]
    leftsum-=a[i]
    if leftsum==rightsum:
        for i in range(i):
            print(a[i],end=' ')
        print()
        for i in range(i+1,n):
            print(a[i],end=' ')
        break
if i==0:
    print('Not possible')