words = []
for i in range(5):
    words.append((map(str, input().split())))
result=""
print(words)
for i in range(5):
    for j in range(len(words[i])):
            print(words[j][i])
            result+=words[j][i]


print(result)
