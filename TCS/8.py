t=int(input())
for _ in range(t):
    l,h=map(int,input().split())
    a = list(map(int,input().split()))
    music=list(map(int,input().split()))
    s,m=0,0
    if music[0] == 0:
        m+=1
        music[0]=1
    for i in range(l):
        if music[i] == 1:
            s=0
        else:
            s+=a[i]
            if s>=h:
                music[i]=1
                m+=1
                s=0
    if music[l-1] == 0:
        m+=1
        music[l-1]=1
    print(m)