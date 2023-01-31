"""
문제해결방법
1. 1, 2, 3, 4, 5, 6, 7, 8
2. 해당 번호가 짝수면 -> 그 다음 라운드 num // 2
3. 해당 번호가 홀수면 -> 그 다음 라운드 num // 2 + 1 
4. 해당 번호들이 1 or 2가 될때까지 2로 나눠주고, answer ++
5. 중간에 같은 조에서 만나는 경우 -> 1차이나고, 4로 나누면 나머지 == 3 (규칙발견)
5. 3, 7, 11, 15, 19 -> 4로 나누면 나머지 == 3 (규칙발견)
"""
def solution(n,a,b):
    answer = 0
    # 두수가 1차이가 날때
    if a + 1 == b or b + 1 == a:
        # 1차이가 나면서 같은 "조"일때
        if (a+b) % 4 == 3:
            answer += 1
            return answer
    
    while True:
        if a % 2 == 0:
            a = a // 2
        else:
            a = a // 2 + 1
            
        if b % 2 == 0:
            b = b // 2
        else:
            b = b // 2 + 1
            
        answer += 1
        
        #끝까지 간 경우
        if (( a == 1 or a == 2) and (b == 1 or b ==2)):
            answer += 1
            break
        else:
            # 가다가 같은조가 된 경우
            if a + 1 == b or b + 1 == a:
                if (a+b) % 4 == 3:
                    answer += 1
                    break
        
    return answer

"""
다른 사람의 간단한 풀이
-> 내 수식에서 조금만 바꾸면 생각할 수 있는 문제였는데, 아쉽다.

def solution(n,a,b):
    round = 0 
    while a != b:
        round += 1
        a = (a+1) // 2
        b = (b+1) // 2
    return round

"""