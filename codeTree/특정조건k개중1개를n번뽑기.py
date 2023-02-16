"""
문제

1이상 K이하의 숫자를 하나 고르는 행위를 N번 반복하여 나올 수 있는 모든 서로 다른 순서쌍을 구해주는 프로그램을 작성해보세요.
단, 연속하여 같은 숫자가 3번 이상 나오는 경우는 제외합니다.

예를 들어 K이 2, N이 3인 경우 다음과 같이 6개의 조합이 가능합니다.

1 1 2

1 2 1

1 2 2

2 1 1

2 1 2

2 2 1

입력 형식
첫째 줄에 K와 N이 공백을 사이에 두고 주어집니다.

1≤K≤4

1≤N≤8

출력 형식
조건을 만족하는 서로 다른 순서쌍의 개수 만큼의 줄에 걸쳐 한 줄에 하나씩 순서쌍의 상태를 공백을 사이에 두고 출력합니다. 
이때 앞에서 부터 봤을 때 사전순으로 앞선 순서쌍부터 출력합니다.

입출력 예제
예제1

입력:

2 1

출력:

1
2

예제2
입력:

2 3

출력:

1 1 2
1 2 1
1 2 2
2 1 1
2 1 2
2 2 1

제한
시간 제한: 1000ms
메모리 제한: 80MB
"""


k, n = tuple(map(int, input().split()))

result = []
def permutation(cnt):
    if cnt == n:
        for elem in result:
            print(elem, end = " ")

        print()
        return 

    for i in range(1, k +1):
        if cnt > 1 and result[-1] == result[-2] == i:
            continue
        result.append(i)
        permutation(cnt + 1)
        result.pop()

permutation(0)