a,b,c,d,e = input().split()
if e=='x':
    print(eval(a+b+c))
elif a=='x':
    if b == '+':
        print(int(e)-int(c))
    elif b == '-':
        print(int(e)+int(c))
elif c=='x':
    if b=='+':
        print(int(e)+int(a))
    elif b=='-':
        print(int(a)-int(e))

#method 2
def eval_algebra(eq):
    a,b,c,d,e=eq.split()
    if e=='x':
        return(eval(a+b+c))
    elif a=='x':
        return int(e)-int(c) if b=='+' else int(e)+int(c)
    elif c=='x':
        return int(e)-int(a) if b=='+' else int(a)-int(e)
s=input()
print(eval_algebra(s))