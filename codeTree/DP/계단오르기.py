MAX_N = 1000
MOD = 10007

# 변수 선언 및 입력:
n = int(input())
dp = [0] * (MAX_N + 1)

# 초기 조건 설정
# dp[i] = k -> i번째 까지 오르는데 k가지의 방법
# 0 : 1가지 방법, 1 : 방법없음, 2 : 1가지 방법(2사용), 3 : 1가지 방법(3사용)
dp[0] = 1
dp[1] = 0
dp[2] = 1
dp[3] = 1

# 점화식에 따라 dp값 채우기
# dp[i] = dp[i - 2] + dp[i - 3]
for i in range(4, n + 1):
    dp[i] = dp[i - 2] + dp[i - 3]

print(dp[n] % MOD)