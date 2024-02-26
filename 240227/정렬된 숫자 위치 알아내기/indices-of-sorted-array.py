n=int(input())

arr=list(map(int, input().split()))

class Index:
    def __init__(self, idx1, idx2):
        self.idx1=idx1
        self.idx2=idx2

arr_with_idx=[]

for idx, elem in enumerate(arr, start=1):
    arr_with_idx.append((elem, idx))

arr_with_idx.sort(key=lambda x: x[0])

rank_of_idx=[]

for idx, rank in enumerate(arr_with_idx, start=1):
    rank_of_idx.append((rank[1], idx))

last_arr=[
    Index(idx1, idx2) for idx1, idx2 in rank_of_idx
]
last_arr.sort(key=lambda x: x.idx1)

for number in last_arr:
    print(number.idx2, end=' ')