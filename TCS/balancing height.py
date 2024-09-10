t =int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    possible = True
    C = []
    for i in range(n):
        if A[i] <= B[i]:
            C.append(A[i] if A[i] <= B[i] else B[i])
        else:
            possible = False
            break
    if possible:
        sum_A = sum(A)
        sum_B = sum(B)
        sum_C = sum(C)
        if sum_A <= sum_C <= sum_B:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")