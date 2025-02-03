H, M = map(int, input().split())

if M > 45 :
    M = M-45
elif M < 45:
    H -=1
    M = 60 - (45 - M)
elif M == 45:
    M = 0

if H < 0:
    H +=24


print(H, M)

