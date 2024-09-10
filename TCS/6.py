t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))[:n]
    p=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[j]!=0 and l[i] +l[j] == l[i] // l[j] or l[i]!=0 and l[j] + l[i] == l[j] // l[i]:
                p+=1
    print(p) 