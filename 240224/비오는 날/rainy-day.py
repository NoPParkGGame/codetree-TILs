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
    date=date.split('-')    # date비교를 위해 
    date[0]=int(date[0])
    arr_info.append(information(date, day, weather))

min_val=sys.maxsize
min_num=0
for i in range(n):
    if arr_info[i].weather=='Rain':
        if arr_info[i].date[0]<min_val:
            min_val=arr_info[i].date[0]
            min_num=i

arr_info[min_num].say()