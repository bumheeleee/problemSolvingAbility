"""
문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/76502

다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.

(), [], {} 는 모두 올바른 괄호 문자열입니다.
만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다. 
예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다. 
예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.
대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다. 
이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 
return 하도록 solution 함수를 완성해주세요.

입출력 예
s	       result
"[](){}"	3
"}]()[{"	2
"[)(]"	    0
"}}}"	    0
입출력 예 설명

입출력 예 #1
다음 표는 "[](){}" 를 회전시킨 모습을 나타낸 것입니다.
x	s를 왼쪽으로 x칸만큼 회전	올바른 괄호 문자열?
0	"[](){}"	O
1	"](){}["	X
2	"(){}[]"	O
3	"){}[]("	X
4	"{}[]()"	O
5	"}[](){"	X
올바른 괄호 문자열이 되는 x가 3개이므로, 3을 return 해야 합니다.

입출력 예 #2
다음 표는 "}]()[{" 를 회전시킨 모습을 나타낸 것입니다.
x	s를 왼쪽으로 x칸만큼 회전	올바른 괄호 문자열?
0	"}]()[{"	X
1	"]()[{}"	X
2	"()[{}]"	O
3	")[{}]("	X
4	"[{}]()"	O
5	"{}]()["	X
올바른 괄호 문자열이 되는 x가 2개이므로, 2를 return 해야 합니다.

입출력 예 #3
s를 어떻게 회전하더라도 올바른 괄호 문자열을 만들 수 없으므로, 0을 return 해야 합니다.

입출력 예 #4
s를 어떻게 회전하더라도 올바른 괄호 문자열을 만들 수 없으므로, 0을 return 해야 합니다.

문제해결방법 
1. deque를 하나 선언하고 s를 삽입 => s_dq
2. 0 ≤ x < (s의 길이) popleft(), append()를 해서 올바른 괄호인지 확인한다
3. 확인하는 로직 : check_dq선언 -> s_dq의 원소를 하나씩 check_dq에 삽입, check_dq의
크기가 2이상이면 뒤에 원소 두개를 가져옴 모양이 "()", "{}", "[]"이면 pop(), pop()
4. check_dq의 크기가 0 -> answer ++
"""
from collections import deque

def solution(s):
    answer = 0
    s_dq = deque(s)
    
    for i in range(len(s_dq)):
        check_dq = deque() 
        if i == 0:
            for el in s_dq:
                check_dq.append(el)
                if len(check_dq) >= 2:
                    bracket1 = check_dq[len(check_dq) - 2]
                    bracket2 = check_dq[len(check_dq) - 1]
                    
                    bracket = bracket1 + bracket2
                    if (bracket == "()" or bracket == "{}" or 
                       bracket == "[]"):
                        check_dq.pop()
                        check_dq.pop()
                    
            if len(check_dq) == 0:
                answer += 1
        else:
            elem = s_dq.popleft()
            s_dq.append(elem)
            for el in s_dq:
                check_dq.append(el)
                if len(check_dq) >= 2:
                    bracket1 = check_dq[len(check_dq) - 2]
                    bracket2 = check_dq[len(check_dq) - 1]
                    
                    bracket = bracket1 + bracket2
                    if (bracket == "()" or bracket == "{}" or 
                       bracket == "[]"):
                        check_dq.pop()
                        check_dq.pop()
                    
            if len(check_dq) == 0:
                answer += 1
    
    return answer


print(solution("[](){}"))