# words = []
# for i in range(5):
#     words.extend(list(map(str, input().split())))
# result=""
# # print(words)
#
# for i in range(5):
#     for j in range(len(words[i])):
#         print(words[j][i],end="")
#         # result+=words[j][i]
#
# print(result)


words = []

words = [input() for i in range(5)]

print(words)


for i in range(5):
    for j in range(len(words[i])):
        print(words[j][i], end='')

# #Aa0FfBb1GgCc2HhDd3IiEe4Jj