A=list(input())
n=len(A)
ans=0

for i in range(n-3):
    for j in range(i+2, n-1):
        if A[i]=='(' and A[i+1]=='(':
            if A[j]==')' and A[j+1]==')':
                ans+=1
print(ans)