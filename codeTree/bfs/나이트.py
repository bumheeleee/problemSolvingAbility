"""
나이트는 다음과 같이 노란색 위치를 기준으로 검은색 8곳으로 움직임이 가능합니다. 
n * n 격자 위에서 격자를 벗어나지 않고 나이트가 시작점에서 도착점까지 가는 데 걸리는
최소 이동 횟수를 구하는 프로그램을 작성해보세요.

dxs = [-2, -1, 1, 2, 2, 1, -1, -2]
dys = [1, 2, 2, 1, -1, -2, -2, -1]

위의 방식대로 이동한다고 한다.

입력 형식
첫 번째 줄에는 격자의 크기를 나타내는 n이 주어집니다.

두 번째 줄에는 나이트의 시작 위치 (r1, c1)와 끝 위치 (r2, c2)가 각각 공백을 사이에 두고 주어집니다.
이는 r1행 c1열 에서 r2행 c2열로 이동해야 함을 의미합니다. (1 ≤ r1, c1, r2, c2 ≤ n)

1 ≤ n ≤ 100
출력 형식
시작 위치에서 도착 위치까지 나이트가 도달하는 데 필요한 최소 이동 횟수를 출력합니다. 불가능하다면 -1을 출력합니다.

입출력 예제
예제1
입력:

5
3 3 3 2

출력:

3

예제2
입력:

3
3 3 1 1

출력:

4

제한
시간 제한: 1000ms
메모리 제한: 80MB

"""

import sys
from collections import deque

n = int(input())
st_row, st_col, ed_row, ed_col = tuple(map(int, input().split()))

step = [
    [-1] * n
    for _ in range(n)
]

visited = [
    [False] * n
    for _ in range(n)
]

def can_go(x, y):
    """
    1. 범위안에 있는지 확인
    2. visitied가 false
    """
    if (0 <= x < n and 0 <= y < n) and visited[x][y] == False:
        return True
    else:
        return False



def bfs():
    global q
    dxs = [-2, -1, 1, 2, 2, 1, -1, -2]
    dys = [1, 2, 2, 1, -1, -2, -2, -1]

    while q:
        row, col = q.popleft()
        for dx, dy in zip(dxs, dys):
            curr_x, curr_y = row + dx, col + dy
            if can_go(curr_x, curr_y):
                q.append((curr_x, curr_y))
                visited[curr_x][curr_y] = True
                # 생성 노드보다 값이 한개 증가 (이게 가장 핵심 포인트)
                step[curr_x][curr_y] = step[row][col] + 1
        
        if step[ed_row - 1][ed_col - 1] != -1:
            break


q = deque()
q.append((st_row - 1, st_col - 1))
visited[st_row - 1][st_col - 1] = True
step[st_row - 1][st_col - 1] = 0
bfs()

print(step[ed_row - 1][ed_col - 1])
