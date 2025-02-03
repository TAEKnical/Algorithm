# n =int(input())
#
# # n/2 줄까지 찍어야 할 별의 개수 = 2*n-1
# # n/2 줄까지 앞공백 = n-1
#
#
# for i in range(1,2*n,2):
#     for j in range(n-i//2-1, 0 ,-1):
#         print(" ", end="")
#     for j in range(i):
#         print("*",end="")
#     print()
#
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(" ", end="")
#     for j in range(2*(n-i)-1):
#         print("*", end="")
#     print()


#다른 풀이
n = 5
for i in range(1, n):
    print(" "*(n-i) + '*'*(2*i-1))
for i in range(n, 0, -1):
    print(" "*(n-i) + '*'*(2*i-1))