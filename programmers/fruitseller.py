from collections import deque


def solution(k, m, score):
    answer = 0

    count = len(score) // m
    boxes = [[] for _ in range(count)]
    score = deque(sorted(score, reverse=True))

    while (len(score) >= m):
        box = [score.popleft() for _ in range(m)]
        answer += (min(box) * m)

    return answer

# #better
# for i in range(m - 1, len(score), m):
#     result += score[i] * m
