"""
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 
흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

입출력 예
numbers	return
"17"	3
"011"	2

입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

11과 011은 같은 숫자로 취급합니다.

순열 문제 => 17, 71은 다름
"""

def is_prime(num):
    check = True
    if num == 0 or num == 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            check = False
            break
            
    return check
    
def solution(numbers):
    answer = 0
    nums = []
    result = []
    len_numbers = len(numbers)
    visited = [False] * len_numbers
    
    #백트래킹으로 구현한 조합
    def combination(depth, end):
        if depth == end:
            val = "".join(nums)
            result.append(int(val))
            return
        
        for i in range(len_numbers):
            if visited[i] is False:
                visited[i] = True
                nums.append(numbers[i])
                combination(depth + 1, end)
                nums.pop()
                visited[i] = False
    
    for i in range(1, len_numbers + 1):
        combination(0, i)
    
    #중복 제거
    result_li = list(set(result))
    
    #값 출력
    for i in range(len(result_li)):
        if is_prime(result_li[i]):
            answer += 1
            
    return answer