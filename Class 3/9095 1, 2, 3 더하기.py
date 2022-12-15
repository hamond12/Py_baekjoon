# 테스트 케이스 개수
t = int(input())

# n을 1,2,3의 합으로 나타내는 방법의 수 출력
def f(n):

    if n == 1:  # n=1일 땐
        return 1  # 방법이 한 ㅜ가지

    elif n == 2:  # n=2일 땐
        return 2  # 방법이 두 가지 (1+1, 2)

    elif n == 3:  # n=3일 땐
        return 4  # 방법이 네 가지 (1+1+1, 1+2, 2+1, 3)

    else:  # n>=4이면
        # f(4)=f(1)+f(2)+f(3)=1+2+4=7
        return f(n-3)+f(n-2)+f(n-1)


for i in range(t):
    n = int(input())
    print(f(n))
