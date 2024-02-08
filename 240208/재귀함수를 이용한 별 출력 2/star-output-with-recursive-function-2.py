N=int(input())

def make_star(n):
    if n==0:
        return
    print('* ' * n)
    make_star(n-1)
    print('* ' * n)
    
make_star(N)