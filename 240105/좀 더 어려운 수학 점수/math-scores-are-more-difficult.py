A=input().split() #A=[95, 90]
B=input().split() #B=[95, 80]
A_math, A_eng= int(A[0]),int(A[1]) #A_math= 95, A_eng=90
B_math, B_eng=int(B[0]), int(B[1]) #B_math= 95, B_eng= 80

if A_math==B_math: #True
    if A_eng>B_eng: #90>80
        print('A')
    else:
        print('B')
elif A_math>B_math:
    print('A')
else:
    print('B')