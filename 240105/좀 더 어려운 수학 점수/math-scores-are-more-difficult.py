A=input().split()
B=input().split()
A_math, A_eng= int(A[0]),int(A[1])
B_math, B_eng=int(B[0]), int(A[1])

if A_math==B_math:
    if A_eng>B_eng:
        print('A')
    else:
        print('B')
elif A_math>B_math:
    print('A')
else:
    print('B')