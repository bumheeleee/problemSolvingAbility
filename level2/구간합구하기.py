"""
문제
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

출력
총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.
"""

# 문제 url : https://www.acmicpc.net/problem/11659

# 접근 => 우선 리스트에 주어져 있는 수들의 부분합 리스트를 만든다.
# Ex) [1,2,3,4,5] 리스트1번
#     [1,3,6,10,15] 리스트2번 , 이과정은 리스트2번 전에수와 리스트1의 현재 수를 더해서 만들어준다.
# 그러면 M이 주어질때는 어떻게? ex) 2 4 라고 하면 2+3+4 이렇게 해야되는데 이걸 부분합 리스트를 만들어 논 것을 이용해서 해보자
# 인덱스조심(나는 0으로 시작하는것으로 함.) 2 4 라고 하면 부분합 리스트에선 3 - 0 이라면 된다
# 규칙 => 앞에는 주워진 리스트 보다 1적은놈 뒤는 2적은놈.

import sys
# 입력
N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))  #개수 N개인 수 입력 받기

# 누적합 구하기

# psum list만들기
psum = [0] * N # 크기가 N인 배열 만들기
psum[0] = a[0] # psum의 첫번째는 직접 받는 수 밖에 없음.
for i in range(1,N):
    psum[i] = psum[i-1] + a[i]

# 쿼리 입력받기
for _ in range(M):
    l, r = map(int,sys.stdin.readline().split())

    if l == 1:  # 처음부터 r까지 더하는 것읻 => 걍 psum[r-1]
        answer = psum[r-1]
    else:
        answer = psum[r-1] - psum[l-2]

    print(answer)