n1_A, n2_B = tuple(map(int,input().split()))

A_arr=list(map(int,input().split()))

B_arr=list(map(int,input().split()))
Y_or_N=0
for i in range(len(A_arr)):
    if A_arr[i:len(B_arr)+i]==B_arr:
        Y_or_N=1

if Y_or_N==1:
    print('Yes')
else:
    print('No')
        

'''
수열 A의 처음부터 끝까지 돌아야함
수열 A1부터 시작해 len(B)만큼의 개수만큼 B와 비교해야함
그것을 A````n1 이 될 때까지 반복, 단 n1이 수열 A의 인덱스를 벗어나면 안되기에
제한을 걸어줘야 함

'''