score = {"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}
count = 20
sum_score = 0
sum_point = 0
for i in range(20):
    subject, point, grade = map(str, input().split())
    if grade=="P":
        count-=1
        continue
    sum_score += float(point)*score[grade]
    sum_point += float(point)
print(sum_score/sum_point)

