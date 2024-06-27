'''num1=int(input('enter number 1 '))
num2=int(input('enter number 2 '))'''
def gcd(num1,num2):
    factors1 = []
    factors2 = []

    for i in range(2,num1+1):
        if num1%i==0:
            factors1.append(i)

    for i in range(2,num2+1):
        if num2%i==0:
            factors2.append(i)

    gcd=None
    for i in factors1:
        for j in factors2:
            if i==j:
                gcd = i
    return gcd
#print(f"GCD of {num1} and {num2} is {gcd}")
num1 = 12
num2 = 30
lcm = ((num1*num2)//gcd(12,30)) # type: ignore
print(lcm)
