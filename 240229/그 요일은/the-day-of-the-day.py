m1, d1, m2, d2= tuple(map(int, input().split()))
given_day=input()

month, day= m1, d1

day_of_month=[0,31,29,31,30,31,30,31,31,30,31,30,31]

day_of_week=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

for idx, elem in enumerate(day_of_week):
    if given_day==elem:
        index_given_day=idx # A요일의 인덱스 반환

def total_day(m, d):
    elapsed_day=0
    for i in range(1, m):
        elapsed_day+=day_of_month[i] # m-1달 까지는 모든 날 다 포함
    
    elapsed_day+=d # m 번째 달에는 day까지만 포함 즉, 1월 1일부터 총 흐른 날

    return elapsed_day

elapsed_day = total_day(m2,d2) - total_day(m1,d1) # 두 날짜 사이의 값 계산
'''
while  index_given_day> 0:  # A요일이 리스트 가장 앞에 오도록 리스트 변경

    day_of_week=day_of_week[1:] + [day_of_week[0]]

    index_given_day-=1
    
'''
cnt_A=0
for i in range(elapsed_day+1):
    if i%7==index_given_day:
        cnt_A+=1
print(cnt_A)