n= int(input())

class students:
    def __init__(self, name, s1, s2, s3):
        self.name=name
        self.s1=s1
        self.s2=s2
        self.s3=s3
    
given_input=[
    tuple(input().split())
    for _ in range(n)
]

class_val=[
    students(name, int(s1), int(s2), int(s3))
    for (name, s1, s2, s3) in given_input
]

class_val.sort(key=lambda x: (x.s1 + x.s2 + x.s3))

for score in class_val:
    print(score.name, score.s1, score.s2, score.s3)