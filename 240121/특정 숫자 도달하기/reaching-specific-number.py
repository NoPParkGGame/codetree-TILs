arr=list(map(int,input().split()))
sum_val=0
cnt_val=0
for elem in arr:
    if elem<250:
        sum_val+=elem
        cnt_val+=1
    else:
        break
print(sum_val,f'{sum_val/cnt_val:.1f}')