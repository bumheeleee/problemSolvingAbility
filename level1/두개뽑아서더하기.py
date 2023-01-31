"""
문제링크 : https://school.programmers.co.kr/learn/courses/30/lessons/68644
"""

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        elem1 = numbers[i]
        for elem2 in numbers[i+1:]:
            num = elem1 + elem2
            if num not in answer:
                answer.append(num)
    answer.sort()
    return answer