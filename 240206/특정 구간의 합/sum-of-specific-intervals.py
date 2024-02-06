n, m = tuple(map(int, input().split()))

list_A = [0] + list(map(int, input().split()))

def sum_part():
    for _ in range(m):
        sum_val=0
        a, b = tuple(map(int, input().split()))
        for i in range(a, b+1):
            sum_val+= list_A[i]
        print(sum_val)
sum_part()