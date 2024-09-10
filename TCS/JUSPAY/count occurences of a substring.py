s=input()
sub=input()
pos=-1
c=0
while True:
    pos=s.find(sub,pos+1,len(s))
    if pos == -1:
        break
    else:
        print(f"Found position:{pos}")
        c+=1
if c==0:
    print(-1)
else:
    print(f"No of occurences:{c}")