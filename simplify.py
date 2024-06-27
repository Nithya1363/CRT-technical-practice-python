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
    print(f"GCD of {num1} and {num2} is {gcd}")
    return gcd
n=21
d=49
res = gcd(21,49)
print(f"Simlplify of {21}/{49} is {n//res}/{d//res}") # type: ignore