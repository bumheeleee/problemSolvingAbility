"""
문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12901

문제 설명
2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 
두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 
요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT입니다. 
예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

제한 조건
2016년은 윤년입니다.
2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)
입출력 예
a	b	result
5	24	"TUE"

문제해결방법
1. [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 1월부터 12월까지
2. n월 m일 이면 -> 일수 : n-1월까지의 일수 합 + m
3. 일수 % 7 -> 0 : 금 1 : 토 ~ 6 : 목 
"""
def solution(a, b):
    answer = ''
    month = a
    day = b
    total_days = 0
    
    list_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    for i in range(0, month - 1):
        total_days += list_days[i]
        
    total_days = total_days + day - 1
    answer = day_of_week[total_days % 7]
    
    return answer

print(solution(5, 24))