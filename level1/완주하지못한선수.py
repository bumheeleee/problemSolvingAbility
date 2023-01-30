"""
problem : https://school.programmers.co.kr/learn/courses/30/lessons/42576?language=python3
"""

def solution(participant, completion):
    answer = ''
    check = dict()
    
    for elem in completion:
        if elem not in check:
            check[elem] = 1
        else:
            check[elem] += 1
    
    for elem in participant:
        if elem in check:
            check[elem] -= 1
            if check[elem] == -1:
                answer = elem
                break
        else:
            answer = elem
            break
    
    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))