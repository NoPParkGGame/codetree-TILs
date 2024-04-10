r, c= tuple(map(int, input().split()))

arr=[
    input().split()
    for _ in range(r)
]
# 색이 다른지 판별하는 함수
def is_diff(moved_axis):
    global cur_axis
    return cur_axis!=moved_axis

cur_axis= arr[0][0]
ans=0

for i in range(1, r):
    for j in range(1, c):   # 1,1 부터 한 칸씩 완전탐색 진행
        second_detect=False # 2차 탐색은 기본 False
        if is_diff(arr[i][j]):  # 색이 다르다면 
            second_detect=True  # 2차 탐색 허가
            
        if second_detect:   # 2차 탐색 허가가 났다면
            for k in range(i+1, r):
                for l in range(j+1, c):
                    cur_axis=arr[i][j]
                    third_detect=False
                    if is_diff(arr[k][l]):  # 색이 다른 곳을 또 발견했다면
                        third_detect=True

                    if third_detect:
                        cur_axis=arr[k][l]
                        for o in range(k+1, r):
                            for p in range(l+1, c):
                                if is_diff(arr[o][p]):
                                    ans+=1
print(ans)