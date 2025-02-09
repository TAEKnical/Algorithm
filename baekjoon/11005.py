dec, N = map(int,input().split())

result = ""
alp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


while dec:
    result = alp[dec%N] + result
    dec //= N

print(result)
