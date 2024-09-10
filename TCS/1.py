n=int(input())
arr=list(map(int,input().split()))[:n]
d,m=map(int,input().split())
print(sum([i for i in range(n-m+1) if sum(arr[i:i+m])==d]))
#n,arr,(d,m) = int(input()), list(map(int, input().split())), map(int, input().split())
print(sum(sum(arr[i:i+m]) == d for i in range(n-m+1)))