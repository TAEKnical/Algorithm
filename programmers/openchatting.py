def solution(records):
    answer = []
    nick_dict = {}
    for i in records:
        record = i.split(" ")
        action = record[0]
        uid = record[1]

        if action == "Enter" or action == "Change":
            nick_dict[uid] = record[2]

    for i in records:
        record = i.split(" ")
        action = record[0]
        uid = record[1]

        if action == "Enter":
            answer.append(nick_dict[uid] + "님이 들어왔습니다.")
        elif action == "Leave":
            answer.append(nick_dict[uid] + "님이 나갔습니다.")

    return answer