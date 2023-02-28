"""
행렬의 곱셈
문제 설명
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
곱할 수 있는 배열만 주어집니다.


문제 해결 방법
[1, 4]
[3, 2] 
[4, 1]

[3, 3]
[3, 3]
행렬의 곱셈 -> (3, 2) * (2, 2) -> (3, 2)
arr2[0][0] arr2[1][0] arr2[2][0], arr2[0][1], arr2[1][1] arr2[2][1]
문제 해결 방법
1. arr1은 행, arr2은 열 곱하기


[2, 3, 2]
[4, 2, 4]
[3, 1, 4]

[5, 4, 3]
[2, 4, 1]
[3, 1, 1]

"""
def solution(arr1, arr2):
    answer = []
        
    # arr1의 행 개수만큼 반복
    for i in range(len(arr1)):
        temp = []
        # arr2의 열 개수만큼 반복
        for j in range(len(arr2[0])):
            sum_val = 0
            # arr1의 열과 arr2의 행과 같음
            for k in range(len(arr2)):
                sum_val += arr1[i][k] * arr2[k][j]
            temp.append(sum_val)
        answer.append(temp)
    return answer 

