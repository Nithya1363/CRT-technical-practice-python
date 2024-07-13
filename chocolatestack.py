def solution (N, C):
    s=[]
    r=[]
    for i in range(N):
        if C[i]>0:
            s.append(C[i])
        else:
            sold=s.pop()
            r.append(sold)
    return r
N = int(input())
C = list(map(int, input().split()))
out_ = solution(N, C)
print (' '.join(map(str, out_)))