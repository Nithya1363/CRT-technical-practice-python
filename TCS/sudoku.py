#Method -1:
def sudoku(l):
    k = []
    for i in range(len(l)):
        k += l[i]
    n = len(k)
    j = set(k)
    if n == len(j):
        return 1
    else:
        return 0
l = []
for i in range(3):
    k = list(map(int,input().split()))
    l.append(k)
print(sudoku(l))
#Method 2
l=[]
l1=[]
for i in range(3):
  l.append([])
  for j in range(3):
    n=int(input())
    l[i].append(n)
    l1.append(n)
if len(set(l1))==len(l1):
  print(1)
else:
  print(0)

#Method 3
def valid_sudoku(l):
    numbers = [num for row in l for num in row]
    if sorted(numbers) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return 1  
    else:
       return 0
l = [list(map(int, input().split())) for _ in range(3)]
print(valid_sudoku(l))
