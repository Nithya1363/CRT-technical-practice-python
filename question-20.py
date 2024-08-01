#Question 20
t=[[],[],[],[]]
for i in range(3):
    for j in range(3):
        t[i].append(int(input()))
        if t[i][-1] not in range(1,101):
            print("Invalid input")
for i in range(3):
    t[3].append(((t[2][i]+t[1][i]+t[0][i])//3))
m=max(t[3])
for i in range(3):
    if t[3][i]<70:
        print(f"Trainee {i+1} is unfit")
    elif t[3][i]==m:
        print(f"Trainee Number: {i+1}")