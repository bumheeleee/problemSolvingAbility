"""
문제
n개의 숫자가 주어졌을 때, 자주 등장한 순으로 k개의 숫자를 출력하는 프로그램을 작성해보세요.

입력 형식
첫 번째 줄에는 원소의 개수 n과 k가 공백을 사이에 두고 주어집니다.

두 번째 줄에는 n개의 원소가 공백을 사이에 두고 주어집니다.

1 ≤ k ≤ n ≤ 100,000

1 ≤ 주어지는 원소 값 ≤ 10**9
 

출력 형식
가장 많이 등장한 숫자부터 k개의 숫자를 공백을 사이에 두고 출력합니다. 
만약 등장 횟수가 동일한 경우라면 값이 더 큰 숫자부터 출력합니다.
중복을 제외했을 때 원소의 개수가 k보다 작은 경우는 없다고 가정해도 좋습니다.

입출력 예제
예제1
입력:

5 2
1 1 3 2 3

출력:

3 1 

제한
시간 제한: 1000ms
메모리 제한: 80MB

"""

n, k = tuple(map(int, input().split()))

arrs = list(map(int, input().split()))

cnt = {}

for elem in arrs:
    if elem not in cnt:
        cnt[elem] = 1
    else:
        cnt[elem] += 1

# 2번째방법 : 아예 정렬을 하고 pop해서 key값만 가져오자
# x[1] : cnt가 높은순(value), x[0] : cnt가 동일할때 수(key)가 높은순
cnt = sorted(cnt.items(), key=lambda x: (x[1], x[0]))

for _ in range(k):
    elem = cnt.pop()
    print(elem[0], end = " ")

# 답은 맞지만, 시간 초과 발생(k번 max 찾는게 오래걸림)
# for _ in range(k):
#     mx_cnt = 0
#     mx_elem = 0
#     for elem, elem_cnt in cnt.items():
#         if (elem_cnt, elem) > (mx_cnt, mx_elem):
#             mx_elem = elem
#             mx_cnt = elem_cnt
            
#     cnt[mx_elem] = -1
#     print(mx_elem, end = " ")
    