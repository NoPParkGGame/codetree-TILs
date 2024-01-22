arr=list(map(int,input().split())) #리스트 만들기
new_arr=[]  
for i in range(1,10):
    new_arr.append(i)   #새 리스트에 1부터 9까지 선언

for i in range(len(arr)):
    arr[i]=arr[i]//10   # 기존 리스트의 십의자리숫자의 리스트로 변환

for elem in new_arr: # 1부터 9까지 중
    cnt=0   
    for sec_elem in arr:
        if elem==sec_elem:  #만약 기존리스트와 숫자가 같으면 카운트+1
            cnt+=1  
            
    print(f'{elem} - {cnt}')