n=int(input())
arr_A=list(map(int, input().split()))
arr_B=list(map(int, input().split()))

if sorted(arr_A)==sorted(arr_B):
    print('Yes')
else:
    print('No')