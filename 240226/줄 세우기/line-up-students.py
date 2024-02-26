n=int(input())

class Students():
    def __init__(self, hei, wei, num):
        self.hei=hei
        self.wei=wei
        self.num=num

given_input=[
    input().split()+[i+1]
    for i in range(n)
]

arr_student=[
    Students(int(hei), int(wei), num) for hei, wei, num in given_input
]

arr_student.sort(key=lambda x: (-x.hei, -x.wei, x.num))

for info in arr_student:
    print(info.hei, info.wei, info.num)