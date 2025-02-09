# 1/1
# 1/2 2/1
# 3/1 2/2 1/3
# 1/4 2/3 3/2 4/1

import copy

x = int(input())
dif = copy.deepcopy(x)
line = 1
while True:
    if dif-line <= 0:
        break;
    dif -= line
    line +=1


result = []
for i in range(1,line+1):
    # 1/x 2/x-1 3/x-2 ...
    if line%2 == 0:
        result.append(f"{i}/{line-(i-1)}")
    # x/1 x-1/2 x-2/3 ...
    else:
        result.append(f"{line-(i-1)}/{i}")

print(result[dif-1])