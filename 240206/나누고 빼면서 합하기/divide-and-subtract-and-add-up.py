n, m = tuple(map(int, input().split()))

list_A = list(map(int, input().split()))

def sum_m():
    sum_val=0
    global m
    while m >= 1:
        sum_val+=list_A[m-1]
        if m%2==0:
            m//=2
        else:
            m-=1
   
    return sum_val

print(sum_m())