k,n,m=map(int,input().split()) #k=과자값, n=과자 수, m=동수 전재산
r=k*n-m #받아야 하는 돈 = 과자값(k*n) - 현재 재산
if(r>0): print(r) 
else : print(0) #돈 필요없으면 0출력
