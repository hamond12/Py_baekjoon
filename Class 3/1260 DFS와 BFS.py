# popleft 사용을 위한 deque선언
from collections import deque

# 정점 개수, 간선 개수, 탐색시작 정점번호
n, m, v = map(int, input().split())

# 그래프(크기, 개수: 정점개수+1만큼)
graph = [[0]*(n+1) for i in range(n+1)]

# 방문한 곳 체크
visit1 = [0] * (n+1)  # dfs의 방문표시
visit2 = [0] * (n+1)  # bfs의 방문표시

# 입력 받는 두 값의 열행렬에 1 삽입
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# 깊이 우선 탐색
def dfs(v):

    # 방문한 곳 1 넣고 출력
    visit1[v] = 1
    print(v, end=' ')

    # 1~정점개수 만큼 반복
    for i in range(1, n+1):
        # v와 인접한 곳 찾고 방문하지 않았다면 함수 다시 실행
        if visit1[i] == 0 and graph[v][i] == 1:
            dfs(i)

# 넓이우선 탐색
def bfs(v):

    # deque선언 후 탐색번호 넣기
    q = deque()
    q.append(v)

    # 탐색표시
    visit2[v] = 1

    # q가 텅빌 때까지
    while q:

        # 탐색번호를 q[-1]로 설정 후 그 값 q에서 삭제
        v = q.popleft()
        print(v, end=' ')

        # 1~정점개수 만큼 반복
        for i in range(1, n+1):
            # v와 인접한 곳 찾고 방문하지 않았다면
            if visit2[i] == 0 and graph[v][i] == 1:
                # 큐에 정점번호 추가 후
                q.append(i)
                # 방문표시
                visit2[i] = 1

dfs(v)
print() #개행
bfs(i)
