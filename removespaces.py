s = "  this is python crt  "
start = None
end = None
for i in range(len(s)):#to get first non space char index
    if s[i] != " ":
        start = i
        break
for i in range(len(s)-1,-1,-1):#to get last non space char index
    if s[i] != " ":
        end = i
        break
print(s[start:end+1]) # type: ignore
print(s.strip())