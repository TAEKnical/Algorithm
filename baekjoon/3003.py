donghyuk = list(map(int, input().split()))
normal = [1,1,2,2,2,8]
answer = []
for i in range(len(normal)):
    answer.append(normal[i]-donghyuk[i])

print(*answer)