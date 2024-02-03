string_A= input()

string_B= input()
cnt=0
while True:
    string_A=string_A[-1]+string_A[:-1]
    cnt+=1
    if string_A==string_B:
        break
    if cnt==0:
        break

if cnt==0:
    print(-1)
else:
    print(cnt)