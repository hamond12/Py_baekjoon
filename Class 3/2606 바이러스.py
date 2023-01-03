n=int(input()) #컴퓨터 수
l=int(input()) #연결선 수
graph=[[] for i in range(n+1)] #그래프 선언
visit=[0]*(n+1) #방문표시 선언

#네트워크에 연결된 컴퓨터 번호 쌍 입력받기
for i in range(l):
    a,b=map(int,input().split())

    #n번째 컴퓨터와 연결된 컴퓨터를 나타내는 그래프 만들기
    graph[a]+=[b] #a에 b연결
    graph[b]+=[a] #b에 a연결

#깊이 우선 탐색
def dfs(l):
    visit[l]=1 #방문표시
    for i in graph[l]: #n번째 컴퓨터에 연결된 컴퓨터들 중
        if visit[i]==0: #방문하지 않은 곳이 있다면
            dfs(i) #재귀

dfs(1) #바이러서는 1번 컴퓨터부터 퍼짐
print(sum(visit)-1) #그러므로 1번 컴퓨터 제외 후 결과값 출력
