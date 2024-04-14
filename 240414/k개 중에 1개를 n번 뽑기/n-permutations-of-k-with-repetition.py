k, n= tuple(map(int, input().split()))
answer=[]

def print_now():
    for elem in answer:
        print(elem, end=' ')
    print()


def make_twin(curr_num):
    
    if curr_num==n+2:
        print_now()
        return

    for i in range(1, k+1):
        answer.append(i)
        make_twin(curr_num + 1)
        answer.pop()        

make_twin(n)