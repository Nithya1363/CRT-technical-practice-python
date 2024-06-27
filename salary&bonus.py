salary = int(input())
yrs = int(input())
if yrs>=5:
    bonus = (5/100) * salary
    total = salary + bonus
    print(f"Bonus: {bonus} and total: {total}")
else:
    print("not applicable for bonus") 