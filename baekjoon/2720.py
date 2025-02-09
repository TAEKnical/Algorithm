n = int(input())
result = []
for _ in range(n):
    change = int(input())

    quarter = change // (25)
    change = change%25

    dime = change // (10)
    change = change%10

    nickel = change // 5
    change = change%5

    penny = change
    result.append([quarter,dime,nickel,penny])

for ans in result:
    print(*ans)