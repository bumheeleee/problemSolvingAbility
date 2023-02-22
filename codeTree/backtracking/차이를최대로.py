#순열 백트래킹
"""
문제
N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

입력
첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 
배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

출력
첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

예제 입력 1 
6
20 1 15 8 4 10

예제 출력 1 
62
"""

n = int(input())

arr = list(map(int, input().split()))


nums = []
result = []
visited = [False] * n
def permutation(cnt):
    if cnt == n:
        result.append(tuple(nums))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            nums.append(arr[i])
            permutation(cnt + 1)
            nums.pop()
            visited[i] = False

def cal(arr):
    ans = 0
    for i in range(len(arr) - 1):
        ans += abs(arr[i] - arr[i + 1])

    return ans

permutation(0)

ans_list = []
for elem in result:
    ans_list.append(cal(elem))

print(max(ans_list))





