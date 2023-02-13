"""
문제
숫자 0, 1로만 이루어진 n * n 격자가 주어졌을 때, k개의 시작점으로부터 상하좌우 인접한 곳으로만 이동하여 도달 가능한 칸의 수를 구하는 프로그램을 작성해보세요. 
숫자 0은 해당 칸이 이동할 수 있는 곳임을, 숫자 1은 해당 칸이 이동할 수 없는 곳임을 의미합니다.

입력 형식
첫 번째 줄에는 격자의 크기를 나타내는 n과 시작점의 수를 나타내는 k 값이 공백을 사이에 두고 주어집니다.
두 번째 줄 부터는 n개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자가 순서대로 공백을 사이에 두고 주어집니다.
그 다음 줄 부터는 k개의 줄에 걸쳐 각 시작점의 위치 (r, c)가 공백을 사이에 두고 주어집니다. (r, c)는 r행 c열 위치가 시작점 중 하나임을 의미합니다. 
모든 시작점의 위치에 적혀있는 숫자는 0이고, 시작점끼리 서로 겹치지 않게 주어진다고 가정해도 좋습니다. (1 ≤ r ≤ n, 1 ≤ c ≤ n)

1 ≤ n ≤ 100

1 ≤ k ≤ n * n

출력 형식
시작지점으로부터 방문이 가능한 서로 다른 칸의 수를 출력합니다.

입출력 예제
예제1
입력:

3 2
0 0 0
0 0 1
1 0 0
1 1
1 2
출력:

7
예제2
입력:

4 2
0 1 0 0
0 1 0 0
0 1 1 1
0 1 0 0
1 4
4 4
출력:

6
"""

# 1. BFS로 풀이하는 방법

import sys 
from collections import deque

n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

start_locs = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(m)
]

visited = [
    [False] * n
    for _ in range(n)
]

def can_go(x, y):
    """
    1. grid 범위안에 있어야됨
    2. visited == false
    3. grid[x][y] == 0
    """
    if (0 <= x < n and 0 <= y < n) and visited[x][y] == False and grid[x][y] == 0:
        return True
    else:
        return False

def bfs():
    global q
    global answer 

    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            curr_x, curr_y = x + dx, y + dy
            if can_go(curr_x, curr_y):
                visited[curr_x][curr_y] = True
                q.append((curr_x,curr_y))
                answer += 1

answer = 0
q = deque()
for loc in start_locs:
    x, y = tuple(loc)
    cha_x, cha_y = x - 1, y - 1

    if can_go(cha_x, cha_y):
        q.append((cha_x, cha_y))
        visited[cha_x][cha_y] = True
        answer += 1
        bfs()
    
print(answer)



# # 1. DFS 풀이하면 시간초과 발생...O(N**2)

# import sys 
# from collections import deque

# n, m = tuple(map(int, input().split()))

# grid = [
#     list(map(int, sys.stdin.readline().split()))
#     for _ in range(n)
# ]

# start_locs = [
#     list(map(int, sys.stdin.readline().split()))
#     for _ in range(m)
# ]

# visited = [
#     [False] * n
#     for _ in range(n)
# ]

# def can_go(x, y):
#     """
#     1. grid 범위안에 있어야됨
#     2. visited == false
#     3. grid[x][y] == 0
#     """
#     if (0 <= x < n and 0 <= y < n) and visited[x][y] == False and grid[x][y] == 0:
#         return True
#     else:
#         return False

# def dfs(x, y):
#     global answer

#     dxs = [0, 1, 0, -1]
#     dys = [1, 0, -1, 0]

#     for dx, dy in zip(dxs, dys):
#         curr_x, curr_y = x + dx, y + dy
#         if can_go(curr_x, curr_y):
#             visited[curr_x][curr_y] = True
#             answer += 1
#             dfs(curr_x, curr_y)



# answer = 0
# for elem in start_locs:
#     x, y = tuple(elem)

#     cha_x, cha_y = x-1, y-1
#     if can_go(cha_x, cha_y):
#         visited[cha_x][cha_y] = True
#         answer += 1
#         dfs(cha_x, cha_y)

# print(answer)