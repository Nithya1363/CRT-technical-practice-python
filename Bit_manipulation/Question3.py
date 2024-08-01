def num(n):
    res=n[0]
    for i in range(1,len(n)):
        res^=n[i]
    return res
if __name__ == '__main__':
    a=list(map(int,input().split()))
    print(num(a))