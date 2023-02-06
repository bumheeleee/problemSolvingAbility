"""
<문제>
n * m 크기의 이차원 영역의 좌측 상단에서 출발하여 우측 하단까지 뱀에게 물리지 않고 탈출하려고 합니다. 
이동을 할 때에는 반드시 아래와 오른쪽 2방향 중 인접한 칸으로만 이동할 수 있으며, 뱀이 있는 칸으로는 이동을 할 수 없습니다. 
예를 들어 <그림 1>과 같이 뱀이 배치 되어 있는 경우 실선과 같은 경로로 탈출을 할 수 있습니다. 
이 때 뱀에게 물리지 않고 탈출 가능한 경로가 있는지 여부를 판별하는 코드를 작성해보세요.


입력 형식
첫 번째 줄에는 n과 m이 공백을 사이에 두고 주어지고,

두 번째 줄부터 (n+1)번째 줄까지는 각 행에 뱀이 없는 경우 1, 뱀이 있는 경우 0이 입력으로 공백을 사이에 두고 주어집니다. 
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

0
예제2
입력:

5 5
1 0 1 1 1
1 0 1 0 1
1 1 1 0 1
1 0 1 1 1
0 1 1 0 1
출력:

1

"""

import sys

n, m = tuple(map(int, sys.stdin.readline().split()))

problem_lists = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

visited = [
    [0] * m
    for _ in range(n)
]

def dfs(st_x, st_y):
    if problem_lists[st_x][st_y]:
        under_x, under_y = st_x + 1, st_y
        left_x, left_y = st_x, st_y + 1
        
        if can_go(under_x, under_y):
            visited[under_x][under_y] = 1
            dfs(under_x, under_y)
            
        if can_go(left_x, left_y):
            visited[left_x][left_y] = 1
            dfs(left_x, left_y)
        
def can_go(x, y):
    # 1. 사각형 범위안에 있어야함
    # 2. 뱀을 만나지 말아야함
    # 3. 방문하지 않은 곳
    if (0 <= x < n and 0 <= y < m) and problem_lists[x][y] and not visited[x][y]:
        return True
    else:
        return False

st_x = 0
st_y = 0
visited[st_x][st_y] = 1
dfs(st_x, st_y)

print(visited[n-1][m-1])
