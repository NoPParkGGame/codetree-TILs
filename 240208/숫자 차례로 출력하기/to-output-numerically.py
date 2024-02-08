N=int(input())

def print_num(n):
    if n==0:
        return
    print_num(n-1)
    print(n,end=' ')

def print_num_reversed(n):
    if n==0:
        return
    print(n,end=' ')
    print_num_reversed(n-1)

print_num(N)
print()
print_num_reversed(N)