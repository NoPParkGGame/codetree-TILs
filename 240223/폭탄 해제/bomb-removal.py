class bomb:
    def __init__(self, code, color, second):
        self.code=code
        self.color=color
        self.second=second
    
    def say(self):
        print(f'code : {self.code}')
        print(f'color : {self.color}')
        print(f'second : {self.second}')

code, color, second = tuple(input().split())

info=bomb(code, color, int(second))

info.say()