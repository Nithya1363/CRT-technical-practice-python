#Armstrong number
n = int(input())
l=len(str(n))
temp = n
rem =0
s=0
while n>0:
    rem=n%10
    s+=rem**l
    n=n//10
if temp == s:
    print(f"{s} is an Armstrong number")
else:
    print(f"{s}is not an Armstrong number")