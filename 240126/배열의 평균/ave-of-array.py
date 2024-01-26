arr_2r_4c=[
    list(map(int,input().split()))
    for _ in range(2)
]
total_sum_val=0
total_count=0
for elem in arr_2r_4c:
    print(sum(elem)/len(elem),end=' ')
    total_sum_val+=sum(elem)/len(elem)
    total_count+=1
print()

for j in range(4):
    sum_val=arr_2r_4c[0][j]+arr_2r_4c[1][j]
    print(sum_val/2,end=' ')
    total_sum_val+=sum_val/2
    total_count+=1

print()

print(f'{total_sum_val/total_count:.1f}')