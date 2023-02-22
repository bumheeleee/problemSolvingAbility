"""
문제 : 최소 경로로 탈출 하기

n * m 크기의 이차원 영역의 좌측 상단에서 출발하여 우측 하단까지 뱀에게 물리지 않고 탈출하려고 합니다. 
이동을 할 때에는 반드시 상하좌우에 인접한 칸으로만 이동할 수 있으며, 뱀이 있는 칸으로는 이동을 할 수 없습니다. 
예를 들어 [그림 1]과 같이 뱀이 배치 되어 있는 경우 실선과 같은 경로로 탈출을 할 수 있습니다. 
탈출 가능한 경로의 최단 거리를 출력하는 코드를 작성해보세요.


입력 형식
첫 번째 줄에는 n과 m이 공백을 사이에 두고 주어지고,

두 번째 줄부터 (n+1)번째 줄까지는 각 행에 뱀이 없는 경우 1, 뱀이 있는 경우 0이 입력으로 공백을 사이에 두고 주어집니다.
시작과 끝 지점에는 뱀이 주어지지 않는다고 가정해도 좋습니다.

2 ≤ n, m ≤ 100
출력 형식
좌측 상단에서 출발하여 우측 하단까지 이동 가능한 경로 중 최단 거리를 출력합니다. 불가능한 경우 -1을 출력합니다.

입출력 예제
예제1
입력:

5 5
1 0 1 1 1
1 0 1 0 1
1 0 1 1 1
1 0 1 0 1
1 1 1 0 1

출력:

12

예제2
입력:

5 5
1 1 1 1 1
1 0 1 0 1
1 1 1 1 1
1 0 1 0 1
1 1 1 0 1

출력:

8

제한
시간 제한: 1000ms
메모리 제한: 80MB

"""


import sys
from collections import deque

row, col = tuple(map(int, sys.stdin.readline().split()))

grid = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(row)
]

step = [
    [0] * col
    for _ in range(row)
]

visited = [
    [False] * col
    for _ in range(row)
]

def can_go(x, y):
    """
    1. 범위안에 있는지 확인
    2. grid 1만 갈 수 있음
    3. visitied가 false
    """
    if (0 <= x < row and 0 <= y < col) and grid[x][y] and visited[x][y] == False:
        return True
    else:
        return False


def bfs():
    global q
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]

    while q:
        row, col = q.popleft()
        for dx, dy in zip(dxs, dys):
            curr_x, curr_y = row + dx, col + dy
            if can_go(curr_x, curr_y):
                q.append((curr_x, curr_y))
                visited[curr_x][curr_y] = True
                # 생성 노드보다 값이 한개 증가 (이게 가장 핵심 포인트)
                step[curr_x][curr_y] = step[row][col] + 1

        
q = deque()

q.append((0,0))
visited[0][0] = True
step[0][0] = 0
bfs()

if step[row-1][col-1] != 0:
    print(step[row-1][col-1])
else:
    print(-1)
