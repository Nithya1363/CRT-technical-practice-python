t=int(input())
for _ in range(t):
    n=int(input())
    em=list(map(int,input().split(' ',n-1)))
    sg,ge=0,[1,]
    for i in range(1,n):
        if (em[i]>em[i-1]):
            x=ge[i-1]+1
            ge.append(x)
        else:
            ge.append(1)
    print(sum(ge))