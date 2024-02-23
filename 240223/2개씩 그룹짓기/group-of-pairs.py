N=int(input())
arr=list(map(int, input().split()))

arr_sort=sorted(arr)

sum_arr=[]

while True:
    new_arr=[arr_sort[0]] + [arr_sort[-1]]
    arr_sort=arr_sort[1:-1]
    sum_val=0
    for elem in new_arr:
        sum_val+=elem
    sum_arr.append(sum_val)
    if len(arr_sort)<1:
        break

print(max(sum_arr))