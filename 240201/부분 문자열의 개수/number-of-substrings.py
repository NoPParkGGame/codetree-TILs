str_A=input()
str_B=input()
cnt=0
for i in range(len(str_A)-len(str_B)+1):
    if str_A[i:i+len(str_B)]==str_B:
        cnt+=1
print(cnt)