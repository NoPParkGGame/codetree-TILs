import sys
class info:
    def __init__(self, codename="", score=0):
        self.codename=codename
        self.score=score

arr=[]

for _ in range(5):
    codename, score = input().split()
    score=int(score)
    arr.append(info(codename, score))

min_val=sys.maxsize
cnt=0
for elem in arr:
    information=elem
    if min_val>information.score:
        min_val=information.score
        num=cnt
    cnt+=1
min_info=arr[num]
print(min_info.codename, min_info.score)