n = int(input()) #게단 수

s = [int(input()) for _ in range(n)] #계단 높이들
dp = [0]*(n) #n번째 계단을 밟았을 때 점수 합

#계단이 2개이하면 점화식 필요 x
if len(s)<=2:
    print(sum(s))

dp[0] = s[0] 
dp[1] = s[0]+s[1]
for i in range(2,n):
    #연속된 세 개 계단 x, 마지막 도착 계단 밟아야 함.
    #dp[3] = max(dp[0]+s[1]+s[3], dp[1]+s[3]) 계단이 4개라면
    #i=3을 대입해 점화식 도출
    dp[i] = max(dp[i-3]+s[i-2]+s[i], dp[i-2]+s[i])

print(dp[n-1]) #배열은 0번지부터
