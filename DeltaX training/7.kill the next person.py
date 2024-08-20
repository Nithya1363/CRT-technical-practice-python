def josephus(n):
    if n==0:
        return False
    arr=list(range(n))
    while len(arr)>1:
        arr.append(arr.pop(0))
        arr=arr[1:]
    return arr.pop()
n=int(input())
print(josephus(n))

#method 2
def joseohus(n):
    people=list(range(n))
    i=0
    while len(people)>1:
        i=(i+1)%len(people)
        people.pop(i)
    return False if n<1 else people[0]
n=int(input())
print(josephus(n))