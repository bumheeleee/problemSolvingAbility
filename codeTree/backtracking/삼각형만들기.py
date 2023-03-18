import sys
# 입력
N = int(sys.stdin.readline()) # 입력이 클때는 이렇게 입력
input_straw = [int(sys.stdin.readline()) for _ in range(N)] # 리스트 내포로 N만큼 입력을 받고 바로 리스트화!

# input_straw 를 정렬하기!
input_straw.sort()

# 삼각형이 될 수만 있으면 가장 큰거 부터 3개 뽑으면 되니까

answer = -1 # 삼각형이 안되면 -1출력이니까
for i in range(N-1,1,-1):   # range(10,1,-1) 이면 10부터 2까지 쭉 찍히는거, 밑에서 list 인덱스 쓸거임으로 N-1이 들어가야한다. 1까지해야 리스트에선 위치가 2(2포함3개-> 최소 삼각형 개수)
    if input_straw[i] < input_straw[i-1] + input_straw[i-2]:
        answer = input_straw[i] + input_straw[i-1] + input_straw[i-2]
        break

print(answer)