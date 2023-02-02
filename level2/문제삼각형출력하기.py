"""
직각 이등변 삼각형의 높이 n이 주어졌을 때, 다음 포맷에 맞게 출력하는 프로그램을 작성해주세요.

오른쪽 위에서 'A' 부터 시작하여 왼쪽 대각선 아래로 문자가 증가하게 출력합니다.
맨 아래에 도착하면 이전에 출력했던 대각선의 출발점 아래부터 다시 위의 규칙에 맞게 진행합니다.
Z 다음에는 다시 A부터 시작합니다.
각 문자 사이에는 공백이 하나 존재합니다.
n이 3일 때

    A
  B D
C E F
입력 형식
첫 번째 줄에 n이 주어집니다.

1 ≤ n ≤ 100
출력 형식
포맷에 맞게 직각 이등변 삼각형을 출력합니다.

입출력 예제
예제1
입력:

3
출력:

    A 
  B D 
C E F
예제2
입력:

7
출력:

            A 
          B H 
        C I N 
      D J O S 
    E K P T W 
  F L Q U X Z 
G M R V Y A B
"""

"""
0 2
1 1
2 0

합 : 6 개수 = 7
0 6
1 5
2 4
3 3
4 2
5 1
6 0

합 : 7 개수 = 6
1 6
2 5
3 4
4 3
5 2
6 1

합 : 8 개수 = 5
2 6
6 2


6 6

"""

from string import ascii_uppercase

n = int(input())
alphabet_list = list(ascii_uppercase)

arr_2d = [
    [""] * n
    for _ in range(n)
]

cnt = 0
st = 0
val = n - 1
for _ in range(n):
    # i = 6, i = 7
    for idx in range(st, n):
        # idx = 0 - 6
        row = idx
        col =  val - row
        arr_2d[row][col] = alphabet_list[cnt]
        cnt += 1
        if cnt >= 26:
            cnt = cnt % 26

    st += 1
    val += 1

for elem in arr_2d:
    for el in elem:
        if el == "":
            print(" ", end = " ")
        else:
            print(el, end = " ")

    print()
