import sys  # sys호출
n=int(input())  # n의 값 입력

class information:
    def __init__(self, date, day, weather):
        self.day=day
        self.date=date
        self.weather=weather    #class를 이용해 값 입력값 입력

    def say(self):
        print(f'{self.date} {self.day} {self.weather}') # 메서드롤 통해 print

arr=[tuple(input().split()) for _ in range(n)]
info_arr=[information(date, day, weather) for date, day, weather in arr]

date_arr=[info_arr[i].date for i in range(n) if info_arr[i].weather=='Rain']
date_arr=sorted(date_arr)

for i in range(n):
    if date_arr[0]==info_arr[i].date:
        info_arr[i].say()