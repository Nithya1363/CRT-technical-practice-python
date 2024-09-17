#Collecting Candies:
t=int(input())
for _ in range(t):
    boxes=int(input())
    candies=list(map(int,input().split()))
    candies.sort()
    sec=[]
    s=candies[0]
    for i in range(1,len(candies)):
        s+=candies[i]
        sec.append(s)
    print(sum(sec))