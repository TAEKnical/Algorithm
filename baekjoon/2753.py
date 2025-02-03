year = int(input())

isLeapyear = 0

if (year%4 == 0 and ((year%100 != 0) or year%400 ==0)):
    isLeapyear = 1

print(isLeapyear)