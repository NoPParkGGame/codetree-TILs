import sys
n=int(input())

arr=list(map(int,input().split()))

max_val=-sys.maxsize
min_val=sys.maxsize

for elem in arr:
    if min_val>elem:
        min_val=elem

for elem in arr[arr.index(min_val):]:
    if max_val<elem:
        max_val=elem

max_val_2=-sys.maxsize
min_val_2=sys.maxsize

for elem in arr:
    if max_val_2<elem:
        max_val_2=elem

for elem in arr[:arr.index(max_val_2)]:
    if min_val_2>elem:
        min_val_2=elem


if max_val==-sys.maxsize and min_val_2==sys.maxsize:
    print(0)
else:
    if max_val-min_val>max_val_2-min_val_2:
        print(max_val-min_val)
    else:
        print(max_val_2-min_val_2)


'''
최솟값에 구매한 후 최대값에 팔아야 함
단, 최솟값 -> 최대값(순서)이 나와야 함
즉, 최댓값을 기준으로 왼쪽에 있는 최솟값을 구하면 되지 않을까?
그리고 index(최댓값) - index(최솟값) 을 하면 되겠다.
*문제 발생: 최댓값-최솟값보다 더 이익을 보는 경우가 생긴다.
그러면 2번째 최댓값- 최솟값을 구해서 두 가지 경우를 비교해야 하나?

--------
이것들 보단 순서를 바꾸어서
최솟값을 기준으로 오른쪽에 있는 최댓값을 구하는 것이 더 낫겠다.

9 4 18 10 2 3 6
*다음과 같은 경우에는 풀리지 않는다. 흠
그러면 위 두 개를 합쳐서 비교를 해볼까?

'''