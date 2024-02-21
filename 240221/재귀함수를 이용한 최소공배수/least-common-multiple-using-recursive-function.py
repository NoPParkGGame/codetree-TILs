n=int(input())

arr=list(map(int, input().split()))


def max_(a, b): #최대공약수 구하기
    if a%b == 0: # a에서 b를 나누었을 때 그 값이 0이면
        return b # 나누는 값이 바로 최대공약수가 된다
    return max_(b, a%b) # 값이 0이 아니라면 a, b의 최대공약수와 b, a%b의 최대공약수가 같음을 이용해 재귀함수 호출

def f(n): #최소 공배수 = 두 수의 곱 / 최대공약수, 즉 두 수씩 나누어서 재귀함수 호출
    if n==1: # n이 1이면 
        if len(arr)==1:
            return arr[0]
        else:
            return (arr[0]*arr[1]) // max_(arr[0],arr[1]) # 0번째 값과 1번째 값의 최소공배수를 return
    

    return f(n-1)*arr[n] // max_(f(n-1), arr[n])   

print(f(n-1))