def snail(depth):
    t=0
    c=0
    flag=0
    while c<=depth:
        for _ in range(30):
            c+=5
            t+=1
            if c>=depth:
                print(t)
                flag=1
                break
        if flag==0:
            c-=30
            t+=10
        else:
            break
d=int(input())
snail(d)