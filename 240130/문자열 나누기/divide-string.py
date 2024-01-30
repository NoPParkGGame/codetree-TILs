n=int(input())

arr=input().split()

new_word=''.join(arr)

num=0
for elem in new_word:
    print(elem,end='')
    num+=1
    if num==5:
        print()
        num=0