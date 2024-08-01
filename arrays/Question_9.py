def find_max_rows(rows):
    max_completed_row= -1
    max_completed_count = 0
    for i,rows in enumerate(rows):
        count_completed = sum(row)
        if count_completed > max_completed_count:
            max_completed_row = i
            max_completed_count = count_completed
        elif count_completed==max_completed_count:
            max_completed_row=-1
    return max_completed_row
t=int(input())
for _ in range(t):
    n,m = map(int, input().split())
    row=[]
    for i in range(n):
        row = list(map(int,input().split()))
        row.append(row)
    max_completed_row=find_max_rows(row)
    print(max_completed_row)