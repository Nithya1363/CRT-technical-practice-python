def supermarket_sales(A, N, B, M):
    MOD = 10**9 + 7  # large prime number for modulo operation
    dp = [[0]*(N+1) for _ in range(B+1)]
    dp[0][0] = 1  # base case: 1 way to make a total price of 0 using 0 items

    for i in range(1, B+1):
        for j in range(1, N+1):
            # if the current item's price is less than or equal to the current total price
            if A[j-1] <= i:
                dp[i][j] = (dp[i][j-1] + dp[i-A[j-1]][j-1]) % MOD
            else:
                dp[i][j] = dp[i][j-1]

    # count the number of baskets in which the Mth item was sold
    count = 0
    for i in range(B, -1, -1):
        if dp[i][M] > 0:
            count = (count + dp[i][M]) % MOD

    return count-1
A = list(map(int,input().split()))
N = int(input())
B = int(input())
M = int(input())
print(supermarket_sales(A,N,B,M))