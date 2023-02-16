#순열 조합 dfs로 백트래킹으로 구하는 연습

lists = [5, 1, 7, 4]

#조합일 경우
[5, 1]
[5, 7]
[5, 4]
[1, 7]
[1, 4]
[7, 4]

#순열일 경우
[5, 1]
[5, 7]
[5, 4]
[1, 5]
[1, 7]
[1, 4]
[7, 5]
[7, 1]
[7, 4]
[4, 5]
[4, 1]
[4, 7]

nums = []
visited = [False] * len(lists)

#순열일 경우, cnt : 반복횟수, m : nPm 의 m
def permutation(cnt, m):
    if cnt == m:
        print(nums)
        return

    for i in range(len(lists)):
        if visited[i] is False:
            visited[i] = True
            nums.append(lists[i])
            permutation(cnt + 1, m)
            nums.pop()
            visited[i] = False

#조합일 경우, cnt : 반복횟수, m : nCm 의 m
def combination(cnt, m, st_idx):
    if cnt == m:
        print(nums)
        return 

    #순열과 다르게 중복을 방지하기 위해 st_idx가 하나씩 증가함
    for i in range(st_idx, len(lists)):
        if visited[i] is False:
            visited[i] = True
            nums.append(lists[i])
            combination(cnt + 1, m, i + 1)
            nums.pop()
            visited[i] = False


combination(0, 3, 0)