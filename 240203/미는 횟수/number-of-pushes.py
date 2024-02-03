string_A= input()

string_B= input()
cnt=0
indicator=True
while True:
    string_A=string_A[-1]+string_A[:-1]
    cnt+=1
    if string_A==string_B:
        break
    if cnt>len(string_A):
        indicator=False
        break

if indicator==False:
    print(-1)
else:
    print(cnt)