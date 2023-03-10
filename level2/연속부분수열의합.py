"""
연속 부분 수열 합의 개수
문제 설명
철호는 수열을 가지고 놀기 좋아합니다. 어느 날 철호는 어떤 자연수로 이루어진 원형 수열의 연속하는 부분 수열의 합으로 만들 수 있는 수가 모두 몇 가지인지 알아보고 싶어졌습니다. 
원형 수열이란 일반적인 수열에서 처음과 끝이 연결된 형태의 수열을 말합니다. 예를 들어 수열 [7, 9, 1, 1, 4] 로 원형 수열을 만들면 다음과 같습니다.

원형 수열은 처음과 끝이 연결되어 끊기는 부분이 없기 때문에 연속하는 부분 수열도 일반적인 수열보다 많아집니다.
원형 수열의 모든 원소 elements가 순서대로 주어질 때, 원형 수열의 연속 부분 수열 합으로 만들 수 있는 수의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
3 ≤ elements의 길이 ≤ 1,000
1 ≤ elements의 원소 ≤ 1,000

입출력 예
elements	result

[7,9,1,1,4]	18
입출력 예 설명
입출력 예 #1
길이가 1인 연속 부분 수열로부터 [1, 4, 7, 9] 네 가지의 합이 나올 수 있습니다.
길이가 2인 연속 부분 수열로부터 [2, 5, 10, 11, 16] 다섯 가지의 합이 나올 수 있습니다.
길이가 3인 연속 부분 수열로부터 [6, 11, 12, 17, 20] 다섯 가지의 합이 나올 수 있습니다.
길이가 4인 연속 부분 수열로부터 [13, 15, 18, 21] 네 가지의 합이 나올 수 있습니다.
길이가 5인 연속 부분 수열로부터 [22] 한 가지의 합이 나올 수 있습니다.
이들 중 중복되는 값을 제외하면 다음과 같은 18가지의 수들을 얻습니다.
[1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15, 16, 17, 18, 20, 21, 22]
"""

def solution(elements):
    # 시간 초과
    # def part_fib_sum(m):
    #     results_lists = []
    #     for i in range(len(elements)):
    #         result_sum = 0
    #         for j in range(i, i+m):
    #             result_sum += elements[j % len(elements)]
    #         results_lists.append(result_sum)

    #     results_lists = list(set(results_lists))
    #     return results_lists

    # answer = 0
    # results = []
    # for i in range(1, len(elements) + 1):
    #     results += part_fib_sum(i)
       
    # answer = len(set(results))

    answer = 0
    init_len = len(elements)
    
    # [7, 9, 1, 1, 4, 7, 9, 1, 1, 4]
    elements = elements * 2
    result_lists = set()

    def part_fib_sum2(m):
        for i in range(init_len):
            result_lists.add(sum(elements[i:i+m]))

    for i in range(1, init_len+1):
        part_fib_sum2(i)

    answer = len(result_lists)
    
    return answer

print(solution([7,9,1,1,4]))