def add_each(n): #n값이 주어졌을 때
    n=str(n) # 그 값을 iterable 한 str 값으로 바꿔주고
    for elem in n: #그 값을 하나씩 돌면서
        if int(elem)==3 or int(elem)== 6 or int(elem) == 9: # 만약 369중 하나라도 있다면 
            return True # True boolean 값을 할당

def multiple_third(a, b):
    cnt=0
    for i in range(a, b+1):
        if i%3==0 or add_each(i):
            cnt+=1

    return cnt

a, b = tuple(map(int, input().split()))


print(multiple_third(a, b))