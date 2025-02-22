import math
N = int(input())

if N==1:
    pass

while(N % 2 == 0):
    print(2)
    N = N // 2

for i in range(3, int(math.sqrt(N))+1, 2):
    while(N % i == 0):
        print(i)
        N = N // i

if N > 1:
    print(N)