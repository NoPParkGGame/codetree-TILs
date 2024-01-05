A=input().split()
B=input().split()
C=input().split()

A_sym, A_temp= A[0], int(A[1])
B_sym, B_temp= B[0], int(B[1])
C_sym, C_temp= C[0], int(C[1])

sym=[A_sym, B_sym, C_sym]
temp=[A_temp, B_temp, C_temp]

A_class=0
n=0
for i in range(0,3):
    if sym[n]=='Y':
        if temp[n]>=37:
            A_class+=1
        else:
            pass #C
    else: 
        pass
    n+=1
if A_class>=2:
    print('E')
else:
    print('N')