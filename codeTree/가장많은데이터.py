"""
문제

가장 많은 데이터
20XP
기본문제
정답률 54%
·
제출 1,001회
·
예상 소요 시간 5분

Like
6
Dislike
아쉬워요
1 Star

Empty
내 리스트에 추가
알파벳 소문자로 이루어진 문자열들이 중복을 허용하여 입력되었을때, 최대로 등장한 문자열의 등장 횟수를 출력하는 프로그램을 작성해보세요.

입력 형식
첫 번째 줄에는 입력될 문자열의 개수 n이 주어집니다.

두 번째 줄부터 n + 1 번째 줄 까지 문자열들이 입력됩니다.

1 ≤ n ≤ 100,000

1 ≤ 문자열의 길이 ≤ 50

출력 형식
첫 번째 줄에 가장 많이 입력된 데이터가 등장한 횟수를 출력합니다.

입출력 예제
예제1
입력:

7
red
red
red
blue
blue
blue
green
출력:

3
"""
n = int(input())

d = dict()
for _ in range(n):
    color = input()
    if color not in d:
        d[color] = 1
    else:
        d[color] += 1

mx_val = 0

for val in d.values():
    if val > mx_val:
        mx_val = val

print(mx_val)
