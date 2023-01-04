#최단경로 구하는 문제는 bfs로 구현
from collections import deque

n,m=map(int,input().split()) #(n,m의 좌표로 이동) -> n = x, m = y

graph=[list(map(int,input())) for _ in range(n)] #n개의 줄만큼 미로 입력받기

#상하좌우 조정값
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#넓이우선탐색
def bfs(x,y): 

    #deque 생성 후 초기값 설정
    q=deque()
    q.append((x,y))
    
    #큐에 남은 값이 있을 때
    while q:

        #x,y 값은 큐의 첫번째 값으로 설정 후 그 값 큐에서 삭제
        x,y = q.popleft() 

        #현재위치에서 상하좌우 탐색
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            #미로를 벗어나지 않고 이동가능한 곳일 때
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                #이동가능한 곳에 1을 추가해서 이동횟수를 표시한다.
                graph[nx][ny] += graph[x][y]
                #큐의 탐색범위 업데이트
                q.append((nx,ny))
                
                """
                이런형태로 바뀌게 됨
                1 1 0 1 1 0     1 2   8  
                1 1 0 1 1 0     2 3   7 8
                1 1 1 1 1 1     3 4 5 6 7 8
                1 1 1 1 0 1     4 5 6 7
                """
    
    #목적지 좌표의 값을 출력
    return graph[n-1][m-1] #배열은 0부터..

print(bfs(0,0)) #초기값 0, 0
