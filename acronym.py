s = input()
s1 = s[0].upper()
for i in range(len(s)):
    if s[i] == " " or s[i]=="-":
        s1+=s[i+1].upper()
print(s1)
