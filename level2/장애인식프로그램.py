"""
문제

자율주행팀 SW 엔지니어인 당신에게 장애물과 도로를 인식할 수 있는 프로그램을 만들라는 업무가 주어졌다.


[그림 1] 지도 예시


우선 [그림 1]과 같이 정사각형 모양의 지도가 있다. 1은 장애물이 있는 곳을, 0은 도로가 있는 곳을 나타낸다.


당신은 이 지도를 가지고 연결된 장애물들의 모임인 블록을 정의하고, 
불록에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 장애물이 좌우, 혹은 아래위로 붙어 있는 경우를 말한다. 
대각선 상에 장애물이 있는 경우는 연결된 것이 아니다.



[그림 2] 블록 별 번호 부여


[그림 2]는 [그림 1]을 블록 별로 번호를 붙인 것이다. 


지도를 입력하여 장애물 블록수를 출력하고, 각 블록에 속하는 장애물의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.


제약조건
N은 정사각형임으로 가로와 세로의 크기는 같으며 5 ≤ N ≤ 25

입력형식
입력 값의 첫 번째 줄에는 지도의 크기 N이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력형식
첫 번째 줄에는 총 블록 수를 출력 하시오.

그리고 각 블록 내 장애물의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

입력예제1복사하기
7
1110111
0110101
0110101
0000100
0110000
0111110
0110000

출력예제1
3
7
8
9
"""

import sys
from collections import deque

n = int(input())

#입력 예시 잘보기 (이거때문에 30분이상 잡아먹음 찾느라....)
grid = [
    list(map(int, str(input())))
    for _ in range(n)
]

visited = [
    [False] * n
    for _ in range(n)
]

result = [
    [0] * n
    for _ in range(n)
]

def block(row, col):
    """
    1. grid 내부에 위치
    1. grid 값이 1이여야지 block로 인식
    2. visited = false
    """
    if (0 <= row < n and 0 <= col < n) and grid[row][col] == 1 and visited[row][col] == False:
        return True
    else:
        return False


def bfs():
    global q
    global cnt

    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]

    while q:
        row, col = q.popleft()
        for dx, dy in zip(dxs, dys):
            curr_row, curr_col = row + dx, col + dy
            if block(curr_row, curr_col):
                visited[curr_row][curr_col] = True
                result[curr_row][curr_col] = cnt
                q.append((curr_row, curr_col))

q = deque()
cnt = 0
for i in range(n):
    for j in range(n):
        if block(i, j):
            cnt += 1
            visited[i][j] = True
            result[i][j] = cnt
            q.append((i, j))  
            bfs()

print(cnt)
answer = []
for i in range(1, cnt + 1):
    ans = 0
    for elem in result:
        for el in elem:
            if el == i:
                ans += 1     

    answer.append(ans)

answer.sort()
for elem in answer:
    print(elem)