t = int(input())
for _ in range(t):
    N = int(input())
    powers = list(map(int, input().split()))
    fights=0
    for i in powers:
        while i%2==0:
            i//=2
            fights+=1
    print(fights)