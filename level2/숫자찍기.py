"""
문제
숫자 모양의 크기 숫자가 주어집니다.

크기가 5일 때의 모양은 다음과 같습니다. 포맷에 맞게 출력하는 프로그램을 작성해주세요.

1 2 3 4 5 
16 17 18 19 6 
15 24 25 20 7 
14 23 22 21 8 
13 12 11 10 9 
입력 형식
첫번째 줄에 숫자가 주어집니다.

1 ≤ 주어지는 숫자 ≤ 100
출력 형식
포맷에 맞게 출력합니다.

입출력 예제
예제1
입력:

5
출력:

1 2 3 4 5 
16 17 18 19 6 
15 24 25 20 7 
14 23 22 21 8 
13 12 11 10 9
예제2
입력:

11
출력:

1 2 3 4 5 6 7 8 9 10 11 
40 41 42 43 44 45 46 47 48 49 12 
39 72 73 74 75 76 77 78 79 50 13 
38 71 96 97 98 99 100 101 80 51 14 
37 70 95 112 113 114 115 102 81 52 15 
36 69 94 111 120 121 116 103 82 53 16 
35 68 93 110 119 118 117 104 83 54 17 
34 67 92 109 108 107 106 105 84 55 18 
33 66 91 90 89 88 87 86 85 56 19 
32 65 64 63 62 61 60 59 58 57 20 
31 30 29 28 27 26 25 24 23 22 21
"""

import sys

def make_outer(arr, startNum, st_idx, size):
    #st_idx = 0부터 시작해 1씩 증가한다. 
    ed_idx = st_idx + size -1

    #arr은 이중배열임
    #첫줄 가로 만들기
    for i in range(st_idx, ed_idx+1):
        arr[st_idx][i] = startNum
        startNum += 1

    #마지막줄 세로 만들기
    for i in range(st_idx+1, ed_idx+1):
        arr[i][ed_idx] = startNum
        startNum += 1

    #마지막줄 가로 만들기
    for i in range(ed_idx-1, st_idx -1, -1):
        arr[ed_idx][i] = startNum
        startNum += 1
    
    #첫줄 세로 만드릭
    for i in range(ed_idx - 1, st_idx, -1):
        arr[i][st_idx] = startNum
        startNum += 1
    
    return startNum
    

size = int(sys.stdin.readline())
 
arr = [
    [0] * size
    for _ in range(size)
]

startNum = 1
st_idx = 0

while size > 0:
    startNum = make_outer(arr, startNum, st_idx, size)
    size -= 2
    st_idx += 1

for elem in arr:
    for el in elem:
        print(el, end= " ")
    print()