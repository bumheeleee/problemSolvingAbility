"""
문제

n개의 정수가 입력으로 주어지고, 이 중 서로 다른 세 개의 위치를 골라 
각 위치에 있는 세 수를 더했을 때 k가 되는 서로 다른 조합의 개수를 출력하는 코드를 작성해보세요.

입력 형식
첫 번째 줄에는 원소의 개수 n과 세 수의 합이 될 k가 공백을 사이에 두고 주어집니다.

두 번째 줄에는 n개의 정수가 공백을 사이에 두고 주어집니다. 숫자가 중복되어 주어질 수 있습니다.

1 ≤ n ≤ 1,000

출력 형식
서로 다른 세 개의 위치를 골라 해당 위치에 있는 세 수를 더했을 때 k가 되는 조합의 개수를 출력합니다.

입출력 예제
예제1
입력:

5 4
1 2 1 4 -1
출력:

3

예제 설명
예제 1의 경우 3개의 위치를 골라 합이 4가 되는 경우는 각각 
(1, 2, 3), (1, 4, 5), (3, 4, 5) 번째 위치에 있는 수들을 골랐을 경우입니다.
각 조합으로부터 결정되는 수들은 순서대로 [-1, 1, 4], [-1, 1, 4], [1, 1, 2]이므로 합이 4가 됨을 알 수 있습니다. 
같은 숫자 쌍이더라도, 고른 숫자의 위치가 다른 경우 다른 조합으로 생각해야함에 유의합니다.
"""

import sys

n, k = tuple(map(int, input().split()))

arrs = list(map(int, input().split()))

cnt_arr = dict()

#각 항목별 개수 만들어줌
for arr in arrs:
    if arr not in cnt_arr:
        cnt_arr[arr] = 1
    else:
        cnt_arr[arr] += 1
        
print(cnt_arr)

ans = 0
for i in range(len(arrs)):
    elem1 = arrs[i]
    #for문 돌면서 사용되는 원소 개수에서 차감
    cnt_arr[elem1] -= 1

    for j in range(i):
        #여기서 elem2는 왜 차감 안해주냐면, elem2는 j의 값이다. 즉 앞에서 이미 다 차감을 해준 애들이라서 안빼줘도됨
        elem2 = arrs[j]
        
        diff = k - elem1 - elem2
        if diff in cnt_arr:
            ans += cnt_arr[diff]        


print(ans)
