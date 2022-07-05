arr=[]
for i in range(10): #10번 반복함
    n=int(input()) 
    arr.append(n%42) #배열에 n을 42로 나눈 나머지값 순서대로 삽입
arr=set(arr) #중복 제거
print(len(arr)) #배열 길이
     
