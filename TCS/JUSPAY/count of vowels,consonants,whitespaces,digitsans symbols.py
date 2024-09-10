from curses.ascii import isalpha


s=input()
v,c,d,w,sy=0,0,0,0,0
for i in s:
    if i.isalpha():
        if i in 'aeiouAEIOU':
            v+=1
        else:
            c+=1
    elif i.isdigit():
        d+=1
    elif i==" ":
        w+=1
    else:
        sy+=1
print(f'Vowels:{v}\nConsonants:{c}\nWhite spaces:{w}\nDigits:{d}\nSymbols:{sy}')