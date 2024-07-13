n = int(input())
if n%3==0:
    print("Pling",end="")
if n%5==0:
    print("Plang",end="")
if n%7==0:
    print("Plong",end="")
if n%3!=0 and n%5!=0 and n%7!=0:
    print(str(n))