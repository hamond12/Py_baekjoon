n=int(input()) #계단 개수

s=[int(input()) for _ in range(n)] #계단 높이
dp=[] #n번째 계단을 밟을 차례의 점수 합

#계단 개수 2개이하일 합처리
if len(s)<=2:
    print(sum(s))

#계단 개수 3개 넘어가면
else:
    dp.append(s[0]) #첫번째 계단
    dp.append(s[0]+s[1]) #두번째 계단
    dp.append(max(s[0]+s[2],s[1]+s[2])) #세번째 계단

    for i in range(3,n):
        #연속된 세 개 계단 x, 마지막 도착 계단 밟아야 함.
        #dp[3] = max(dp[0]+s[2]+s[3], dp[1]+s[3])
        dp.append(max(dp[i-3]+s[i-1],dp[i-2])+s[i])

    print(dp[n-1]) #배열은 0번지 부터
