A,B,V = map(int, input().split())

# Ax-B(x-1)=V
# (A-B)x+B=V
#day = (V-B)/(A-B)
day = (V-B)//(A-B)

if (V-B)%(A-B) == 0:
    print(day)
else:
    print(day+1)
