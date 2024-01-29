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
        abc_list.append(word[-1]) # 문자가 달라지는 시점을 기준으로 공백으로 구획을 나눈 리스트 생성


new_word=''.join(abc_list)  #리스트를 다시 문자열로 합친 후

final_list=new_word.split() # 공백을 기준으로 split 해 같은 문자들 끼리 모아줌

print(len(final_list)*2)

for elem in final_list:
    print(f'{elem[0]}{elem.count(elem[0])}',end='')

'''

문제점: 같은 숫자도 연속해서 나온게 아니면 따로 적어줘야함
word[i]와 word[i+1]의 값이 달라지는 지점에서 블럭을 나눠줘야함
But how?


'''