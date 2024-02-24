import sys  # sys호출
n=int(input())  # n의 값 입력

class information:
    def __init__(self, date, day, weather):
        self.day=day
        self.date=date
        self.weather=weather    #class를 이용해 값 입력값 입력

    def say(self):
        print(f'{"-".join(map(str, self.date))} {self.day} {self.weather}') # 메서드롤 통해 print

arr_info=[] # 각 n번의 입력값 넣을 list 생성
for _ in range(n):
    date, day, weather = input().split()
    date=date.split('-')    # date비교를 위해 각 값을 split해 리스트로 반환
    for i in range(len(date)):
        date[i]=int(date[i])    # 숫자 비교를 위해 date 값들을 int값으로 변환
    arr_info.append(information(date, day, weather))    # 각 값들을 리스트에 추가

min_val_year=sys.maxsize # 최소가 되는 날짜 비교를 위해 min_val 삽입
min_val_month=sys.maxsize
min_val_day=sys.maxsize
min_num=0
for i in range(n):
    if arr_info[i].weather=='Rain': # Rain이 들어가는 경우에만 비교 
        if arr_info[i].date[0]<min_val_year: # 만약 년도 값이 다르다면 바로 반환
            min_val_year=arr_info[i].date[0]
            min_num=i

        elif arr_info[i].date==min_val_year:    #만약 년도 값이 같다면 월을 비교 해야 함
            if arr_info[i].date[1]<min_val_month:
                min_val_month=arr_info[i].date[1]
                min_num=i
            elif arr_info.date[1]==min_val_month:
                min_val_day=arr_info[i].date[2]
                min_num=i

for i in range(n):
    for j in range(len(date)):
        if arr_info[i].date[j]<10:
            arr_info[i].date[j]='0' + str(arr_info[i].date[j])

arr_info[min_num].say()