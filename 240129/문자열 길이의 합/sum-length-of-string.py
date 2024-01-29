n=int(input())

sum_val=0
cnt_val=0
for _ in range(n):
    word=input()
    sum_val+=len(word)
    if word[0]=='a':
        cnt_val+=1

print(sum_val, cnt_val)