def power(a,b):
    if b!=0:
        return a*(power(a,b-1))
    else:
        return 1
if __name__=="__main__":
    a,b=map(int,input().split())
    print(power(a,b))
    