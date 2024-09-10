#Find Money
t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    s = list(map(int,input().split()))
    l = r = 0
    isleft = True
    for i in s:
        if isleft and i == k:
            isleft = False
        else:
            if isleft:
                l += i
            else:
                r += i
    if isleft:
        print(0)
    else:
        print(l,r,sep=" ")