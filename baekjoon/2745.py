N, B = map(str, input().split())
B=int(B)
alp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = 0

for i in range(len(N)):
    idx = alp.find(N[::-1][i])
    result += idx*(B**i)

print(result)