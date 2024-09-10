s=input()
sum=0
for i in s:
    if i.isdigit():
        sum+=int(i)
print(sum)