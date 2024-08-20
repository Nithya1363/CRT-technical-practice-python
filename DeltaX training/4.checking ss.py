'''#print(sum([int(x)for x in input('enter 2 numbers').split()]))
a=['these','are','a',['few','words'],'that','we','will','use']
print(a[3:4][0][1][2])'''
"""condition:
each word must contain atleast 2 instances of s and it must be together (ss)
zero instances of s"""
def check(s):
    ss=[w for w in s if 's' in w]
    for w in ss:
        if w.count('ss')>=1:
            continue
        else:
            return '0'
    return '1'
s=input().lower().split()
print(check(s))


