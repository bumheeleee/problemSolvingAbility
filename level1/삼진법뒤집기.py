"""
문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/68935

문제해결방법
1. 10진법 -> 3진법 변환 함수생성
2. 3진법 -> 10진법 변환 함수생성
3. 문자열 뒤집기

 3 45 0
 3 15 0
 3  5 2
    1
"""

def make_three(num):
    lists = []
    
    if num <= 2:
        return [num]
    
    while num > 2:
        remain = num % 3
        mook = num // 3
        lists.append(remain)
        num = mook
        
        if num == 1 or num == 2:
            lists.append(num)
            
    lists.reverse()
    return lists
        
    
def make_three_to_ten(three_num_lists):    
    answer = 0
    for i in range(len(three_num_lists)):
        answer += three_num_lists[i]*(3**i) 
        
    return answer
    

def solution(n):
    answer = 0
    answer = make_three_to_ten(make_three(n))
    return answer