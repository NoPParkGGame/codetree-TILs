def square_1_9(n):
    num=1
    for _ in range(n):
        for _ in range(n):
            print(num,end=' ')
            if num==9:
                num=1
            else:
                num+=1
        print()

N=int(input())

square_1_9(N)