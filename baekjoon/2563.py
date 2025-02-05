ea = int(input())

paper = [[0]*100 for _ in range(100)]

for _ in range(ea):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j]=1

total=0
for a in range(100):
    total += paper[a].count(1)

print(total)