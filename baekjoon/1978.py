def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

N = int(input())
nums = list(map(int, input().split()))
count = 0

for i in nums:
    if i == 1:
        continue
    if is_prime(i):
        count += 1
print(count)