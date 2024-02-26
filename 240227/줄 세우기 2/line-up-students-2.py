class Students:
    def __init__(self, hei, wei, num):
        self.hei=hei
        self.wei=wei
        self.num=num
n=int(input())

given_input=[
    list(map(int, input().split())) + [i]
    for i in range(1, n+1)
]

arr=[
    Students(hei, wei, num) for hei, wei, num in given_input
]

arr.sort(key=lambda x: (x.hei, -x.wei))

for student in arr:
    print(student.hei, student.wei, student.num)