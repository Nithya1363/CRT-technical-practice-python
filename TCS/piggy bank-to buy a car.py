"""
mon 10 10
tue 11 21
wed 12 33
thu 13 46
fri 14 60
sat 15 75
sun 16 91

mon 11 102
tue 12 114
wed 13 127

"""
def piggybank(c,s,a):
    i=a
    j=0
    days=0
    sum=0
    while s<c-s:
        sum+=i
        i+=1
        j+=1
        if j==7:
            a+=1
            i=a
            j=0
        days+=1
    return days
if __name__=="__main__":
    car=int(input())
    save=int(input())
    amnt=int(input())
    print(piggybank(car,save,amnt))