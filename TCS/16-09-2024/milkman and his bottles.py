def b10(n):
    if n%10==0:
        print(n//10)
    else:
        print(n//10+b751(n))
def b751(n):
    if n==1 or n==5 or 7:
        return 1
    elif n==2 or 6 or 8:
        return 2
    elif n==3 or 9:
        return 3
    elif n==4:
        return 4
    else:
        return 0
t=int(input())
for _ in range(t):
    n=int(input())
    