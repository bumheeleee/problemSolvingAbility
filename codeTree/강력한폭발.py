"""
문제
0, 1로 구성된 n * n 크기의 격자판이 주어집니다. 
1은 해당 위치에 폭탄이 놓이게 됨을 의미합니다. 
1이 써있는 위치에 각각 다음 3가지 중 하나의 폭탄을 선택하여 초토화시킬 지역의 수를 최대화 하려고 합니다.
각 폭탄은 폭탄위치를 포함하여 파란색으로 표시된 영역을 초토화시키게 됩니다.

1 : 해당 [row][col] 기준 위 2개 아래 2개
2 : 해당 [row][col] 상하 좌우 4개
3 : 해당 [row][col] 기준 둥글게 쌓인 8개중 상하좌우 뺀 나머지

초기 격자판의 상태와 폭탄을 놓아야 할 위치들이 주어졌을 때,
가장 많이 초토화시킬 수 있는 영역의 수를 구하는 프로그램을 작성해보세요.

입력 형식
첫 번째 줄에는 격자의 크기를 나타내는 n이 주어집니다.

두 번째 줄 부터는 n개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자가 공백을 사이에 두고 주어집니다. 
각 숫자는 0, 1 중 하나이며 1은 폭탄을 놓아야 하는 위치임을 의미합니다.

1 ≤ n ≤ 20

1 ≤ 폭탄을 놓아야 하는 위치의 수 ≤ 10

출력 형식
가장 많이 폭발에 영향을 받을 수 있는 영역의 수를 출력합니다.

입출력 예제
예제1
입력:

4
0 0 0 0
0 0 1 0
0 1 0 0
0 0 0 0
출력:

9
예제2
입력:

4
0 1 0 0
0 1 0 0
0 1 0 0
0 1 0 0
출력:

12

문제해결방법
1. 폭탄의 종류는 3개가 존재한다.
2. n * n 배열이 주어졌을때, 1의 개수 만큼 3가지 폭탄을 사용해서 값이 가장 큰걸 answer 하면됨

"""
n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def can_go(row, col):
    if (0 <= row < n and 0 <= col < n):
        return True
    else:
        return False

def bomb(arr, row, col, nums):
    if nums == 1:
        for i in range(-2, 3):
            if can_go(row + i, col):
                arr[row + i][col] = 1
        # arr[row-2][col] = 1
        # arr[row-1][col] = 1
        # arr[row][col] = 1
        # arr[row+1][col] = 1
        # arr[row+2][col] = 1

    elif nums == 2:
        arr[row][col] = 1
        dxs = [0, 1, 0, -1]
        dys = [1, 0, -1, 0]

        for dx, dy in zip(dxs, dys):
            curr_row, curr_col = row + dx, col + dy
            if can_go(curr_row, curr_col):
                arr[curr_row][curr_col] = 1

    elif nums == 3:
        arr[row][col] = 1
        if can_go(row-1, col-1):
            arr[row-1][col-1] = 1
        if can_go(row-1, col+1):
            arr[row-1][col+1] = 1
        if can_go(row+1, col+1):
            arr[row+1][col+1] = 1
        if can_go(row+1, col-1):
            arr[row+1][col-1] = 1
            
        # grid[row-1][col+1] = 1
        # grid[row+1][col+1] = 1
        # grid[row+1][col-1] = 1
        # gridarr[row-1][col-1] = 1


def cnt_arr_bomb(arr):
    answer = 0
    for elem in arr:
        for el in elem:
            if el == 1:
                answer += 1
    return answer


permutaion = []
result = []
def solution(cnt):
    global bomb_location
    global cnt_bomb
    
    if cnt == cnt_bomb:
        arr = [
            [0] * n
            for _ in range(n)
        ]

        for i in range(cnt_bomb):
            row = bomb_location[i][0]
            col = bomb_location[i][1] 
            nums = permutaion[i]
            print(f"row, col, nums = {row} {col} {nums}")
            bomb(arr, row, col, nums)            
            
        result.append(cnt_arr_bomb(arr))
        print()
        return

    for i in range(1, 4):
        permutaion.append(i)
        solution(cnt + 1)
        permutaion.pop()

#여기사 시작이다.
bomb_location = [] 
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == 1:
            bomb_location.append((row, col))

cnt_bomb = len(bomb_location)
solution(0)

print(max(result))