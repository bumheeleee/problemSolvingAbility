"""
문제
n * m 크기의 이차원 영역의 좌측 상단에서 출발하여 우측 하단까지 뱀에게 물리지 않고 탈출하려고 합니다. 
이동을 할 때에는 반드시 상하좌우에 인접한 칸으로만 이동할 수 있으며, 뱀이 있는 칸으로는 이동을 할 수 없습니다. 
예를 들어 <그림 1>과 같이 뱀이 배치 되어 있는 경우 실선과 같은 경로로 탈출을 할 수 있습니다. 
이 때 뱀에게 물리지 않고 탈출 가능한 경로가 있는지 여부를 판별하는 코드를 작성해보세요.


입력 형식
첫번째 줄에는 n과 m이 공백을 사이에 두고 주어지고,

두번째 줄부터 (n+1)번째 줄까지는 각 행에 뱀이 없는 경우 1, 뱀이 있는 경우 0이 입력으로 공백을 사이에 두고 주어집니다.
 시작 칸과 끝 칸에는 뱀이 주어지지 않는다고 가정해도 좋습니다.

2 ≤ n, m ≤ 100
출력 형식
좌측 상단에서 출발하여 우측 하단까지 뱀에게 물리지 않고 탈출 가능한 경로가 있으면 1, 없으면 0을 출력합니다.

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

1
예제2
입력:

5 5
1 0 1 1 1
1 0 1 0 1
1 1 1 0 1
1 0 1 1 0
0 1 1 0 1
출력:

0


"""


import sys
from collections import deque

n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

visited = [
    [False] * m
    for _ in range(n)
]

def can_go(x, y):
    # 1. x, y가 n과 m사이의 범위안에 있어야된다.
    # 2. visited는 방문하면 안된다.
    # 3. grid[x][y] == 1만 진행가능하다.
    if (0 <= x < n and 0 <= y < m) and visited[x][y] == False and grid[x][y]:
        return True
    else:
        return False

def bfs():
    global q

    while q:
        x, y = q.popleft()

        #시계방향으로 회전
        dxs = [0, 1, 0, -1]
        dys = [1, 0, -1, 0]

        for dx, dy in zip(dxs, dys):
            curr_x, curr_y = x + dx, y + dy
            if can_go(curr_x, curr_y):
                visited[curr_x][curr_y] = True
                q.append((curr_x, curr_y))



q = deque()

q.append((0,0))
visited[0][0] = True

bfs()

if visited[n-1][m-1]:
    print(1)
else:
    print(0)