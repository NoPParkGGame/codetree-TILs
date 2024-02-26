class Health:
    def __init__(self, name, hei, wei):
        self.name=name
        self.hei=hei
        self.wei=wei

n=int(input())

given_input=[
    input().split()
    for _ in range(n)
]
arr=[
    Health(name, int(hei), int(wei)) for name, hei, wei in given_input
]

arr.sort(key=lambda x: (x.hei, -x.wei))

for each in arr:
    print(each.name, each.hei, each.wei)