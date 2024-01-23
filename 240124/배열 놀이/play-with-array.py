n,q=tuple(map(int,input().split()))

n_arr=list(map(int,input().split()))

for _ in range(q):
    q_arr=list(map(int,input().split()))
    if len(q_arr)==2:
        if q_arr[0]==1:
            print(n_arr[n_arr.index(q_arr[1])])
        else:
            if q_arr[1] in n_arr:
                print(n_arr.index(q_arr[1])+1)
            else:
                print(0)
    else:
        for elem in n_arr[q_arr[1]-1:q_arr[2]]:
            print(elem, end=' ')