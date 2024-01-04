A=input().split()
B=input().split()

A_math, A_eng= int(A[0]), int(A[1])
B_math, B_eng= int(B[0]), int(B[1])

if A_math>B_math and A_eng>B_eng:
    print(1)
else:
    print(0)