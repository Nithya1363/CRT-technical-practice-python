bank = []
principal = int(input())
year = int(input())
for i in range(0, 2): # 2 Banks
    installments = int(input())
    sum = 0
    for i in range(0, installments):
        time, roi = [float(i) for i in input().split()]
        square = pow((1+roi), time*12)
        emi = (principal*(roi)/(1-1/square))
        sum = sum + emi
    bank.append(sum)
if bank[0] < bank[1]:
    print("Bank A")
else:
    print("Bank B")