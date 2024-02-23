code, place, time= input().split()

class Info:
    def __init__(self, code, place, time):
        self.c=code
        self.p=place
        self.t=time

information= Info(code, place, time)

print(f'secret code : {information.c}')
print(f'meeting point : {information.p}')
print(f'time : {information.t}')