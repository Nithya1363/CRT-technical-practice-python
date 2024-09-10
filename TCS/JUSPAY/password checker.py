s=input()
if len(s)>=6:
    if s.isalnum() and '@,#,*,_' in s:
        print(0)
        if s[0] not in [0,1,2,3,4,5,6,7,8,9]:
            print("valid")
    else:
        print("invalid")
else:
    print("Invalid")