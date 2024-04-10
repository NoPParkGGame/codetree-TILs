r, c= tuple(map(int, input().split()))

arr=[
    input().split()
    for _ in range(r)
]
# 색이 다른지 판별하는 함수
def is_diff(moved_axis):
    global cur_axis
    return cur_axis!=moved_axis

ans=0

for i in range(1, r):
    for j in range(1, c):   # 1,1 부터 한 칸씩 완전탐색 진행
        cur_axis= arr[0][0]
        second_detect=False # 2차 탐색은 기본 False
        if is_diff(arr[i][j]):  # 색이 다르다면 
            second_detect=True  # 2차 탐색 허가
            cur_axis=arr[i][j]

        if second_detect:   # 2차 탐색 허가가 났다면
            for k in range(i+1, r-1):
                for l in range(j+1, c-1):
                    cur_axis=arr[k][l]  # 이전 이동한 위치와 도착지점과 색이 다르다면
                    if is_diff(arr[r-1][c-1]) and is_diff(arr[i][j]):
                        ans+=1

print(ans)