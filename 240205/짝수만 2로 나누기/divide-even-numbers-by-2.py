N= int(input())
arr=list(map(int, input().split()))

def even_half(_list):
    for i in range(len(_list)):
        if _list[i]%2 == 0:
            _list[i]//=2

even_half(arr)

for elem in arr:
    print(elem, end=' ')