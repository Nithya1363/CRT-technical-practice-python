age = int(input("enter age : "))
if age > 0:
    if 1<=age<=5 : 
        print("kid")
    elif 6<=age<=10:
        print("child")
    elif 11<=age<=17 :
        print("boy")
    elif 18<=age<=59 :
        print("man")
    elif 60<=age<=100 :
        print("old")
    elif age > 100 :
        print("immortal")
else:
    print("unborn")