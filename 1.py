print('This is Suresh\'s pc')

#Question 18
for i in range(20):
    m=input()
    l=[]
    if m=="":
        break
    elif int(m) in range(0,120):
        l.append(int(m))
    else:
        print("INVALID INPUT")
        exit()
    fees=0
    for i in l:
        if 0<i<=17:
            fees+=200
        elif 17<i<=40:
            fees+=400
        elif i>40:
            fees+=300
print(f"Total Income {fees} INR")    