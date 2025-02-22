# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
# M = int(input())
# N = int(input())
# result = []
#
# for i in range(M,N+1):
#     if is_prime(i):
#         result.append(i)
#
# if len(result) == 0:
#     print(-1)
#
# else:
#     print(sum(result))
#     print(min(result))


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

M = int(input())
N = int(input())
primes = [i for i in range(M,N+1) if is_prime(i)]

if len(primes) == 0:
    print(-1)

else:
    print(sum(primes))
    print(min(primes))
