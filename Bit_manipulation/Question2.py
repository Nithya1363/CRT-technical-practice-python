def deci(n):
    res=0
    while n!=0:
        if n&1:
            res+=1
        n=n>>1
    return res
if __name__=='__main__':
    n=int(input())
    print(deci(n))