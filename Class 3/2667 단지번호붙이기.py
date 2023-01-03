n=int(input())

graph=[list(map(int,input())) for i in range(n)] #그래프 선언
home = [] #단지별 집 개수
count=0 #단지 내 집 개수

#좌표변경값
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#인접한 집의 개수 탐색 -> 상하좌우 탐색 후 좌표값이 다 0이면 함수 종료 
def dfs(x,y):
  
    if x<0 or x>=n or y<0 or y>=n: #좌표값이 맵을 벗어낫을 때
        return #아무것도 하지않음

    if graph[x][y]==1: #현재좌표에 집이 있다면

        #전역변수(함수 내 사용 변수) 선언
        global count #단지 내 집 개수 
        count +=1 #카운트 하나 늘려주고
        graph[x][y]=0 #현재 좌표값 0으로 초기화

        #좌표값 상하좌우 1씩 바꿔서 탐색
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            dfs(nx,ny)

#그래프의 좌표값이 1일 때만 
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i,j)
            home.append(count)
            count = 0 #단지 내 집 개수 초기화

#문제양식에 맞게 출력
print(len(home))
home.sort() 
for i in range(len(home)):
    print(home[i])
