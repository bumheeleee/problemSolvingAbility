"""
문제
n * n크기의 이차원 영역에 사람 혹은 벽이 놓여져있습니다. 
이 때 상하좌우의 인접한 영역에 있는 사람들은 같은 마을에 있는 것으로 간주한다고 합니다. 
예를 들어 <그림 1> 같이 사람과 벽이 배치되어 있는 경우, 그림 안의 점선과 같이 마을을 나눌 수 있습니다.
이 때 총 마을의 개수와 같은 마을에 있는 사람의 수를 오름차순으로 정렬하여 출력하는 코드를 작성해보세요.

입력 형식
첫 번째 줄에는 n이 주어지고,

두 번째 줄부터 (n+1)번째 줄까지는 각 행에 사람이 있는 경우 1, 벽이 있는 경우 0으로 입력이 공백을 사이에 두고 주어집니다.

5 ≤ n ≤ 25
출력 형식
첫 번째 줄에는 총 마을의 개수를 출력하고,

그 다음 줄부터 각 줄에는 각 마을 내 사람의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하세요.

입출력 예제
예제1
입력:

5
1 0 1 1 1
1 0 0 0 0
0 0 0 1 1
1 1 0 1 1
1 1 0 1 1
출력:

4
2
3
4
6
예제2
입력:

5
0 1 0 0 1
0 1 0 1 1
0 1 0 0 1
0 1 1 1 1
1 0 0 0 0
출력:

2
1
11

문제 해결 방법
1. 이중 for문을 돌면서 모든 영역에서 갈수 있는지를 확인한다.
2. 갈 수 있다고 하면 dfs를 타게한다.

"""

import sys

n = int(sys.stdin.readline())

grid = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

visited = [
    [0] * n
    for _ in range(n)
]

def can_go(row, col):
    # 1. grid안에 위치해야된다.
    # 2. grid값이 0이면 갈 수 없다.
    # 3. 방문했던 곳은 안간다.
    if 0 <= row < n and 0 <= col < n and grid[row][col] and visited[row][col] == 0:
        return True
    else:
        return False


def dfs(st_row, st_col):
    global people 

    # 시계방향으로 회전한다고 했을경우
    d_rows = [0, 1, 0, -1]
    d_cols = [1, 0, -1, 0]
    
    for d_row, d_col in zip(d_rows, d_cols):
        new_row, new_col = st_row + d_row, st_col + d_col
        if can_go(new_row, new_col):
            visited[new_row][new_col] = 1
            people += 1
            dfs(new_row, new_col)

total_group = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        people = 0
        if can_go(i, j):
            visited[i][j] = 1
            people += 1
            dfs(i,j)

        if people != 0:
            total_group.append(people)

print(len(total_group))
total_group.sort()
for elem in total_group:
    print(elem)