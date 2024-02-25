n=int(input())

class students:
    def __init__(self, name, kor, eng, math):
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math

arr=[tuple(input().split()) for _ in range(n)]

student_arr=[students(name, int(kor), int(eng), int(math)) for name, kor, eng, math in arr]

student_arr.sort(key=lambda x: (-x.kor, -x.eng, -x.math) )

for score in student_arr:
    print(score.name, score.kor, score.eng, score.math)