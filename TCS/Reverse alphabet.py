#Method 1
def reverse(s):
    a="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    z="ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjjihgfedcba"
    res=""
    for i in s:
        if i in a:
            res+=z[a.index(i)]
        else:
            res+=i
    return res
s=input()
print(reverse(s))