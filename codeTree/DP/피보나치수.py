"""
DP를 이용한 피보나치 수 구하기

피보나치 수열이란 이전 두 항의 합이 그 다음 항이 되는 수열을 의미합니다.

예를 들어 첫 번째 원 소를 1, 두 번째 원소도 1이라 하면 그 다음 항은 2,3,5,8... 이 됩니다.

N번째 피보나치 수를 구하는 프로그램을 작성해보세요.

"""
n = int(input())

# 기본 피보나치 수열 구하는 방법, 백트래킹 방법(시간이 너무 오래걸림)
def fibbo1(n):
    if n <= 2:
        return 1
    else: 
        return fibbo1(n-1) + fibbo1(n-2)

# 한번 다녀온 수는 기록하는 방법
memo = [-1] * (n+1)
def fibbo2(n):
    if memo[n] != -1:
        return memo[n]

    if n <= 2:
        memo[n] = 1
    else:
        memo[n] = fibbo2(n-1) + fibbo2(n-2)

    return memo[n]


print(fibbo2(n))