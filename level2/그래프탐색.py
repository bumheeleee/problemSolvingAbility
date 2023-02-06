"""
문제
N개의 정점과 M개의 간선으로 이루어진 양방향 그래프가 주어졌을 때,
1번 정점에서 시작하여 주어진 간선을 따라 이동했을 때 도달 할 수 있는 서로 다른 정점의 수를 구하는 프로그램을 작성해보세요. 
(여기서 1번 정점 자기 자신에 도달하는 경우는 가지수에서 제외합니다.)
다음 예시에서 1번 정점은 2,3번 정점과 이어져 있기 때문에 답은 2가 됩니다.



입력 형식
첫 번째 줄에는 N과 M이 공백을 사이에 두고 주어지고,
두 번째 줄부터는 M개의 줄에 걸쳐 (x,y)가 공백을 사이에 두고 주어집니다.
(x,y)는 두 정점 x,y 가 연결되어 있음을 의미합니다. (x,y) 쌍이 동일한 연결관계가 두 번 이상 주어지는 경우는 없다고 가정해도 좋습니다. (1≤x,y≤N)

1≤N≤1,000

0≤M≤min(10,000, 
2
N(N−1))

출력 형식
1번 정점에서 시작하여 주어진 간선을 따라 이동했을 때 도달 할 수 있는 서로 다른 정점의 수를 출력해주세요. 
단, 1번 정점을 제외한 정점의 수를 구해주세요.

입출력 예제
예제1
입력:

5 4
1 2
1 3
2 3
4 5
출력:

2
예제2
입력:

5 4
1 2
4 2
5 3
3 4
출력:

4
"""

# # 변수 선언 및 입력
# n, m = tuple(map(int, input().split()))

# #index를 1번 부터 사용하기 위해 n+1만큼 할당합니다.
# graph = [
#     [0 for _ in range(n + 1)]
#     for _ in range(n + 1)
# ]

# visited = [False for _ in range(n + 1)]
# vertex_cnt = 0


# def dfs(vertex):
#     global vertex_cnt
    
#     # 해당 정점에서 이어져있는 모든 정점을 탐색해줍니다.
#     for curr_v in range(1, n + 1):
#         # 아직 간선이 존재하고 방문한 적이 없는 정점에 대해서만 탐색을 진행합니다.
#         if graph[vertex][curr_v] and not visited[curr_v]:
#             visited[curr_v] = True
#             vertex_cnt += 1
#             dfs(curr_v)
    

# for i in range(m):
#     v1, v2 = tuple(map(int, input().split()))

#     # 각 정점이 서로 이동이 가능한 양방향 그래프이기 때문에
#     # 각 정점에 대한 간선을 각각 저장해줍니다.
#     graph[v1][v2] = 1
#     graph[v2][v1] = 1

# visited[1] = True
# dfs(1)

# print(vertex_cnt)



import sys

n, m = tuple(map(int, sys.stdin.readline().split()))

"""
[
    행 : 노드, 열, 노드랑 연결된 노드
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]
"""

graph = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

visited = [
    False
    for _ in range(n+1)
]

cnt = 0

for _ in range(m):
    node, rel_node = tuple(map(int, sys.stdin.readline().split()))
    graph[node][rel_node] = 1
    graph[rel_node][node] = 1

def dfs(st_node):
    global cnt

    #시작노드와 연관된 노드를 돌면서 방문해줌
    for curr_n in range(1,len(graph[st_node])):
        # curr_n 순서대로 1 ~ 5까지 증가
        if not visited[curr_n] and graph[st_node][curr_n] == 1:
            visited[curr_n] = True
            cnt += 1
            dfs(curr_n)

#현재 시작 노드를 방문했다고 일단 설정을 해줌            
visited[1] = True

dfs(1)
print(cnt)






import sys

n, m = tuple(map(int, sys.stdin.readline().split()))

"""
[
    행 : 노드, 열, 노드랑 연결된 노드
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]
"""

graph = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

visited = [
    False
    for _ in range(n+1)
]

cnt = 0

for _ in range(m):
    node, rel_node = tuple(map(int, sys.stdin.readline().split()))
    graph[node][rel_node] = 1
    graph[rel_node][node] = 1

def dfs(st_node):
    global cnt

    #시작노드와 연관된 노드를 돌면서 방문해줌
    for curr_n in range(1,len(graph[st_node])):
        # curr_n 순서대로 1 ~ 5까지 증가
        if not visited[curr_n] and graph[st_node][curr_n] == 1:
            visited[curr_n] = True
            cnt += 1
            dfs(curr_n)

#현재 시작 노드를 방문했다고 일단 설정을 해줌            
visited[1] = True

dfs(1)
print(cnt)


