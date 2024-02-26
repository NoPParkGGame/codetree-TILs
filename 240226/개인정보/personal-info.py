class Health:
    def __init__(self, name, hei, wei):
        self.name=name
        self.hei=hei
        self.wei=wei

given_input=[
    input().split()
    for _ in range(5)
]

info=[
    Health(name, int(hei), float(wei)) for name, hei, wei in given_input
]

print('name')

info.sort(key=lambda x: x.name)
for guy in info:
    print(guy.name, guy.hei, guy.wei)

print('''
height''')

info.sort(key=lambda x: -x.hei)

for guy in info:
    print(guy.name, guy.hei, guy.wei)