arr=list(map(int,input().split()))

even_arr=arr[1::2]
thrid_arr=arr[2::3]
print(sum(even_arr), f'{sum(thrid_arr)/len(thrid_arr):.1f}')