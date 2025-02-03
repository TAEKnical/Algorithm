N, M = map(int, input().split())

A = []
B = []

for i in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for i in range(N):
    row = list(map(int, input().split()))
    B.append(row)

C = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(A[i][j]+B[i][j])
    C.append(row)

for i in C:
    print(*i)


