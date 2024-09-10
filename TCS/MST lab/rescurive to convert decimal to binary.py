def dectobin(n):
    if n>=1:
        dectobin(n//2)
        print(n%2,end='')
if __name__=="__main__":
    n=int(input())
    dectobin(n)