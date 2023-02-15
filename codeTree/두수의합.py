"""
[해시문제]

문제
n개의 정수가 입력으로 주어지고, 이 중 서로 다른 위치에 있는 두 개의 수를 뽑아 더했을 때 k가 되는 가짓수를 구하는 프로그램을 작성해보세요.

입력 형식
첫 번째 줄에는 원소의 개수 n과 두 수의 합이 될 k가 공백을 사이에 두고 주어집니다.

두 번째 줄에는 n개의 정수가 공백을 사이에 두고 주어집니다. 수가 중복되어 주어질 수 있습니다.

출력 형식
입력으로 주어진 수들 중 서로 다른 위치에 있는 두 개의 수를 골랐을 때 두 수의 합이 k가 되는 가짓수를 출력합니다.

입출력 예제
예제1
입력:

5 9
4 6 5 3 7

출력:

2



n, k = tuple(map(int, input().split()))

problems = list(map(int, input().split()))

answer = 0
for i in range(len(problems)):
    elem1 = problems[i]
    for elem2 in problems[i+1:]:
        if elem1 + elem2 == k:
            answer += 1

print(answer)
위 처럼 풀면 시간초과됨 따라서 다른방법으로 풀어야됨!

[1번째 풀이]
n, k = tuple(map(int, input().split()))

problems = list(map(int, input().split()))

pro_dict = dict()

answer = 0
for problem in problems:
    diff = k - problem 

    # 빼서 만들수 있는 다른 원소가 있는지 확인
    # 여기서 중요한건 첫번째 problem값은 pro_dict에 안들어간다, 그래야만 다른 diff에서 사용가능
    if diff in pro_dict:
        answer += pro_dict[diff]

    if problem not in pro_dict:
        pro_dict[problem] = 1
    else:
        pro_dict[problem] += 1

print(answer)

"""
#[이게더 나한데는 직관적인거 같다.]
n, k = tuple(map(int, input().split()))

problems = list(map(int, input().split()))

pro_dict = dict()

#dict 생성해준다.
for problem in problems:
    if problem not in pro_dict:
        pro_dict[problem] = 1
    else:
        pro_dict[problem] += 1

answer = 0
for problem in problems:
    # 자기 자신은 빼준다.
    pro_dict[problem] -= 1
    diff = k - problem

    if diff in pro_dict:
        answer += pro_dict[diff]

print(answer)