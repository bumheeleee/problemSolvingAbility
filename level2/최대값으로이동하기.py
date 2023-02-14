"""
문제
n*n 크기의 격자에 1이상 100이하의 숫자가 각 칸에 하나씩 주어져 있습니다. 
이때 특정 위치에서 시작하여 아래 조건을 만족하는 숫자의 위치를 찾아 상하좌우로만 이동합니다. 
이렇게 이동하는 것을 k번 반복한 이후의 위치를 구하는 프로그램을 작성해보세요. 
만약 아직 k번을 반복하지 못했지만, 더 이상 새로 이동할 위치가 없다면 움직이는 것을 종료합니다.

한번 이동하기 위한 조건은 다음과 같습니다.

시작 위치에 적혀있는 숫자를 x라고 했을 때, 시작 위치에서 출발하여 인접한 칸들 중 적혀있는 숫자가 x보다 작은 곳으로는 전부 이동이 가능합니다.
다음 그림을 예로 들어보겠습니다. 시작 위치가 4행 3열인 숫자 10이라고 했을 때, 10보다 큰 11을 제외한 인접한 모든 숫자들로 이동이 가능합니다.



1-1. 하지만 만약에 아래 그림처럼 시작 위치의 상하좌우가 시작 숫자(= 10)보다 큰 숫자들(= 11)로 둘러싸여져 있으면 이동이 불가합니다.


1번 조건을 만족하며 도달할 수 있는 칸들에 적혀있는 숫자 중 최댓값으로 이동합니다.


위 그림과 같이 시작 위치에 적혀있는 숫자 10에서 출발하여 인접한 칸들 중 10보다 작지만 그 중 최댓값인 9로 이동을 고려합니다.

2번 조건을 만족하는 숫자가 여러개 일경우, 행 번호가 가장 작은 곳으로 이동합니다. 아래 그림과 같이 2행에 있는 최댓값(= 9)이 두개 있습니다.



2번 조건을 만족하고, 행 번호도 같은 숫자가 여러개 일경우, 열 번호가 가장 작은 곳으로 이동합니다.


결론적으로 4행 3열에서 시작하여 인접한 곳으로 숫자 10보다 작은 곳들로 이동했을 때 갈 수 있는 칸들 중 최대 숫자는 9이고, 그 중 우선순위가 가장 높은 곳은 2행 2열입니다. 따라서 2행 2열 위치로 이동하게 됩니다.


2행 2열 위치를 시작으로 한번 더 움직임을 반복해보면, 2행 2열에서 시작하여 인접한 곳으로 숫자 9보다 작은 곳들로 이동했을 때 갈 수 있는 칸들 중 최대 숫자는 6이고, 그 중 우선순위가 가장 높은 곳은 2행 3열입니다. 따라서 2행 3열 위치로 이동하게 됩니다.




2행 3열 위치를 시작으로 한번 더 움직임을 반복해보면, 2행 3열에서 시작하여 인접한 곳으로 숫자 6보다 작은 곳들로 이동했을 때 갈 수 있는 칸들 중 최대 숫자는 4이고, 4는 2행 1열입니다. 따라서 2행 1열 위치로 이동하게 됩니다.




이렇게 이동하는 것을 k번 반복한 후의 위치를 구하는 프로그램을 작성해보세요. 
아직 k번을 반복하지 못했더라도, 더 이상 새로 이동할 위치가 없다면 움직이는 것을 종료해야함에 유의합니다.

입력 형식
첫 번째 줄에는 격자의 크기를 나타내는 n과 반복할 횟수를 나타내는 k가 공백을 사이에 두고 주어집니다.

두 번째 줄 부터는 n개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자가 순서대로 공백을 사이에 두고 주어집니다.

마지막 줄에는 초기 시작 위치 (r, c)가 공백을 사이에 두고 주어집니다. (r, c)는 r행 c열에서 시작함을 의미합니다.
 (1 ≤ r ≤ n, 1 ≤ c ≤ n)

1 ≤ n, k ≤ 100
출력 형식
이동하는 것을 k번 반복한 이후의 위치 (r, c)를 출력합니다. (r, c)는 최종 위치가 r행 c열임을 의미합니다.

입출력 예제
예제1
입력:

4 2
1 3 2 11
4 9 6 9
2 6 9 8
1 9 10 7
4 3
출력:

2 3
예제2
입력:

4 4
1 3 2 11
4 9 6 9
2 6 9 8
1 9 10 7
4 3
출력:

1 2

"""

import sys
from collections import deque

n, k = tuple(map(int, input().split()))

grid = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

row, col = tuple(map(int, input().split()))

#변환완료
row -= 1
col -= 1

visited = [
    [False] * n
    for _ in range(n)
]

def format_visited():
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            visited[i][j] = False


def can_go(curr_row, curr_col):
    """
    1. 해당 위치의 값보다 숫자가 작아야된다.
    2. grid 내부에 있어야된다.
    3. visited == false
    """
    if (0 <= curr_row < n and 0 <= curr_col < n) and grid[row][col] > grid[curr_row][curr_col] and visited[curr_row][curr_col] == False:
        return True
    else:
        return False

def bfs():
    global q

    dxs = [0 , 1, 0, -1]
    dys = [1, 0, -1, 0]

    check = False
    result = (0,-100,-100)
    answer = (row, col)

    while q:
        now_row, now_col = q.popleft()
        for dx, dy in zip(dxs, dys):
            curr_row, curr_col = now_row + dx, now_col + dy
            if can_go(curr_row, curr_col):
                visited[curr_row][curr_col] = True
                q.append((curr_row, curr_col))
                
                # 1. 값 우선, 2. 행 우선, 3. 열우선 우리 result를 비교
                if result < (grid[curr_row][curr_col], -curr_row, -curr_col):
                    check = True
                    result = (grid[curr_row][curr_col], -curr_row, -curr_col)

    format_visited()

    if check:
        answer = (abs(result[1]), abs(result[2]))

    return answer

q = deque()
ans_row, ans_col = 0, 0

while k:
    k -= 1
    q.append((row, col))
    visited[row][col] = True
    ans_row, ans_col = bfs()

    #2번이상 돌때를 생각해서 만들어줌
    row, col = ans_row, ans_col

print(ans_row + 1, ans_col + 1)