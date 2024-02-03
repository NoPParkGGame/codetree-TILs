string_A= input()

string_B= input()
cnt=0
while True:
    string_A=string_A[-1]+string_A[:-1]
    cnt+=1
    if string_A==string_B:
        print(cnt)
        break
    if cnt>len(string_A):
        print(-1)
        break