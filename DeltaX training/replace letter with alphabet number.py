"""
A to Z --> 65 to 90
a to z --> 97 to 122
0 to 9 --> 48 to 57
ord(char) --> ascii number
chr(int) --> ascii character
"""
def replace(s):
    n=[]
    for i in s:
        if i.isalpha():
            n.append(ord(i)-96)
    return n
s=input().lower()
print(*(replace(s)))