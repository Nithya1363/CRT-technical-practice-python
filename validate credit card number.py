#
s1 = "4539 3195 0343 6467"
r= s1.replace(" ","")
s=0
for i in range(len(r)):
    if i % 2 == 0:
        n= 2*(int(r[i]))
        if n>9:
            s+=n-9
        else:
            s+=n
    else:
        s+=int(r[i])
print(s)
if s%10==0:
    print('valid')
else:
    print('invalid')
