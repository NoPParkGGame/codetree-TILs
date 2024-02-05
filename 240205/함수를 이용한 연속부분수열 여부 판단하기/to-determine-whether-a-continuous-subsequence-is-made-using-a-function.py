n1_A, n2_B = tuple(map(int, input().split()))

list_A = list(map(int, input().split()))

list_B = list(map(int, input().split()))

def is_B_part_of_A(arr_A, arr_B):
    for i in range(len(arr_A)-len(arr_B)+1):
        if arr_A[i:i+len(arr_B)]==arr_B:
            return True
    return False

if is_B_part_of_A(list_A, list_B):
    print('Yes')
else:
    print('No')