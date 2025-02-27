# def solution(X, Y):
#     answer = ''
#
#     # 각 문자마다 수행하므로 O(n^2)
#     # 차라리 각 숫자마다 출현횟수를 세면 O(n)
#     # for i in X:
#     #     if i in Y:
#     #         Y = Y.replace(i, "", 1)
#     #         answer += i
#
#     answer = ''.join(sorted(answer, reverse=True))
#     if answer != '':
#         answer = int(answer)
#         answer = str(answer)
#
#     if answer == '':
#         return '-1'
#
#     if answer == '0':
#         return '0'
#
#     print(answer)
#
#     return answer

def solution(X, Y):
    answer = ''
    x_dict = {}
    y_dict = {}
    common_nums = []

    for num in X:
        x_dict[num] = x_dict.get(num,0)+1

    for num in Y:
        y_dict[num] = y_dict.get(num,0)+1

    for x_num in x_dict:
        if x_num in y_dict:
            common_count = min(x_dict[x_num],y_dict[x_num])
            common_nums.append(x_num*common_count)

    if common_nums == []:
        return '-1'

    answer = ''.join(sorted(common_nums,reverse=True))

    if answer[0] == '0':
        return '0'

    return answer