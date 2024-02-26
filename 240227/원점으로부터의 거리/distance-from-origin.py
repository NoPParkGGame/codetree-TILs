n=int(input())

class Axis:
    def __init__(self, x_val, y_val, num):
        self.x_val=x_val
        self.y_val=y_val
        self.num=num

given_input=[
    tuple(map(int, input().split())) + tuple(str(i+1))
    for i in range(n)
]

arr=[
    Axis(x_val, y_val, num) for x_val, y_val, num in given_input
]

arr.sort(key=lambda x: (abs(x.x_val)+abs(x.y_val), x.num))

for number in arr:
    print(number.num)