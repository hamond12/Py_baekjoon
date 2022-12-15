n = int(input())

s = [int(input()) for i in range(n)]  # 계단높이 받을 배열
dp = [0]*(n)  #n번째 계단을 밟았을 때의 점수 합

# 계단이 2개 이하면 값 다 더해서 출력
if len(s) <= 2:
    print(sum(s))

else:
    dp[0] = s[0]  # 첫번째 계단
    dp[1] = s[0]+s[1]  # 두번째 계단
    for i in range(2, n):  # 세번째 계단 부터 점화식 이용
        dp[i] = max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
        # 연속해서 세 계단을 오를 순 없다
        #dp[3]=max(s[0]+s[1]+s[3], s[1]+s[3])

print(dp[n-1])  # n번째 계단을 밟았을 때의 합
