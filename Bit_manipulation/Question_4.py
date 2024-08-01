"""n = int(input())
res = 0
for i in range(31):
      if (n >> i) & 1 == 1:
              res += (1 << (31 - i))
print(res)"""
def rev(n):
    i=31
    res=0
    while i>=0:
        temp=((n&1<<i)>>i)&1
        res=res|temp<<(31-i)
        i-=1
    return res
if __name__=='__main__':
    n=int(input())
    print(rev(n))