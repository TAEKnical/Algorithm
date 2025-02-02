n, m = map(int, input().split())
basket = [x for x in range(1, n+1)]

for x in range(m):
    i, j = map(int, input().split(" "))
    i = i-1
    j = j-1
    basket[i:j+1] = basket[i:j+1][::-1]

print(*basket)

# *basket은 언패킹 연산자. 이터레이터의 요소를 풀어내서 함수에 하나씩 개별로 전달함.
# print문은 전달받은 요소를 기본적으로 공백으로 구분해서 출력시킴