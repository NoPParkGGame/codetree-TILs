word=input()

abc_list=[]

for i in range(len(word)):
    if i+1<len(word):
        if word[i]==word[i+1]:
            abc_list.append(word[i])
        else:
            abc_list.append(word[i])
            abc_list.append(' ')
    else:
        abc_list.append(word[-1])

print(abc_list)

new_abc_list=[]

for elem in abc_list:
    print(elem, end='')



'''

문제점: 같은 숫자도 연속해서 나온게 아니면 따로 적어줘야함
word[i]와 word[i+1]의 값이 달라지는 지점에서 블럭을 나눠줘야함
But how?


'''