#https://school.programmers.co.kr/learn/courses/30/lessons/12938
def solution(nums):
    answer = 0

    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                if isPrime(nums[i]+nums[j]+nums[k]):
                    print(nums[i],nums[j],nums[k])
                    answer +=1
    return answer

def isPrime(num):
    if num % 2 == 0:
        return False
    for i in range(3,num-1,2):
        if num % i == 0:
            return False
    return True