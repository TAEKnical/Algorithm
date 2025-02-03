A = []
for i in range(9):
    row = list(map(int, input().split()))
    A.append(row)

max_element = -99
max_x = -1
max_y = -1

#대표적인 최댓값 구하기
for i in range(9):
    for j in range(9):
        if A[i][j] > max_element:
            max_element = A[i][j]
            max_x = i+1
            max_y = j+1

print(max_element)
print(max_x, max_y)