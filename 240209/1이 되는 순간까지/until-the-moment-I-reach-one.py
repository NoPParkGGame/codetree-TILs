N= int(input())
def get_num(n, cnt = 0): #카운트 값이 없다면 0을 부여
    if n <= 1:  # 만약 n의 값이 1이 된다면
        print(cnt)

    else:
        if n % 2 == 0: # 만약 짝수라면
            n //= 2    # 2로 나눈 몫을 재귀함수 호출해 새로 판단
            cnt+=1
        
        else:   # 만약 홀수라면
            n //= 3
            cnt+=1
        get_num(n, cnt)

get_num(N)