n,q=tuple(map(int,input().split()))

n_arr=list(map(int,input().split()))

for _ in range(q):
    q_arr=list(map(int,input().split()))
    if len(q_arr)==2:
        a = q_arr[1]
        if q_arr[0]==1:
            print(n_arr[n_arr.index(a)])
        else:
            if a in n_arr:
                print(n_arr.index(a)+1)
            else:
                print(0)
    else:
        a = q_arr[1]
        b = q_arr[2]
        for elem in n_arr[a-1:b]:
            print(elem, end=' ')