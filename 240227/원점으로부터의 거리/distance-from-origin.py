n=int(input())

class Axis:
    def __init__(self, x_val, y_val, num):
        self.x_val=x_val
        self.y_val=y_val
        self.num=num

given_input=[
    list(map(int, input().split())) + [i]
    for i in range(1, n+1)
]

arr=[
    Axis(x_val, y_val, num) for x_val, y_val, num in given_input
]

arr.sort(key=lambda x: (abs(x.x_val)+abs(x.y_val), x.num))

for number in arr:
    print(number.num)