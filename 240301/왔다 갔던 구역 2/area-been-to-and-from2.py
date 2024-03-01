n= int(input()) # n값 입력

direction=[
    input().split()
    for _ in range(n)
] # 주어진 방향들을 리스트에 정렬 -> int로 바꿔줘야함

for a, b in direction: # a값을 int로 바꿔주기 <- 다른 작업과 동시에 해줘도 좋을 듯 하다. -> 비효율적임.
    a=int(a)

offset= n*10 # 음수가 되는 경우를 대비해 offset 설정, n을 이용해 최적화(x<=10 이니까)

x0 = 0 # 가장 초기의 x값 설정.
x0 += offset # 초기의 값에 offset을 더해줌 <- 이 과정은 사실 하나로 만들어도 되나, 원리를 명확히 하기 위함.

arr=[0] * (20 * n +1) # 0으로 이루어진 리스트 선언 

pre_x = x0 # 가장 첫번째는 x0부터 시작함

def dir_R(input_x): # R값이 주어졌을 때 선언, input_x는 a값
    global pre_x
    global offset
    for i in range(pre_x, pre_x + input_x):
        arr[i]+=1
    pre_x= pre_x+input_x # pre_x 값 업데이트

def dir_L(input_x): # L값이 주어졌을 때 선언, input_x는 a값
    global pre_x
    for i in range(pre_x - input_x, pre_x):
        arr[i]+=1
    pre_x= pre_x-input_x

for a, b in direction:
    if b=='R':
        dir_R(int(a))
    else:
        dir_L(int(a))

while 0 in arr: # arr에서 0을 없애 단순화 시킨다. -> 굳이 할 필요는 없다.
    arr.remove(0)

cnt_line=0

for i in range(len(arr)):
    if arr[i]>=2:
        cnt_line+=1

print(cnt_line)

'''
알고리즘:
0으로 이루어진 List를 만든 후 2이상인 놈들을 구함.

R 일 때 -> range(pre_X, pre_x + input_X) 값을 +1 해줘야 함.

L 일 때 -> range(pre_X - input_X, pre_X) 값을 +1 해줘야 함.
여기서 pre_X 는 계속 최신화 되어야 함


-> 각 과정을 함수로 만들어 간단화 작업이 필요.

2이상인 놈들의 총 '구간' (지점X) 를 구해줘야함 즉, (x1, x2-1)

* L일 때 pre_X - input_X <0 일 때를 대비해 Offset을 더해줘야 함.

x의 범위는 10. 만약 1 R, 10 L, 10 L, 10 L 과 같은 값이 주어졌을 때를 대비해
offset은 10으로 설정하면 되지 않을까?
그럼 결과는 -> 11 R, 20 L, 20 L, 20 L 이 되어서 결과가 이상해진다.
흠....주어진 input_X 값에 offset을 더하면 L에서 오류 발생.

시뮬레이션을 해보자.

n=3 (5 R), (10 L), (3 R) 값이 주어졌을 때, 

지점 x0의 변화 값은 5 => -5 => -3 이다 이 결과값에 offset을 더해줘야 15 => 5 => 7 과 같이 양수가 됨.
5 R -> range(0, 5)까지 칠하고
10 L -> range(5-10 => -5, 5) 여기서 오류 발생, 
즉, 주어진 input_X 에 offset을 더하는게 아닌, 애초에 지점x0이 x=0 값에서 시작하면 안됨.
즉, x0에  offset을 더해줘야 함. 

***문제 상황: n의 최댓값은 100, xn의 최댓값은 10 이므로 offset을 100*10 으로 해주면
수행시간이 너무 커짐 -> 주어진 n값 * 10을 offset으로 설정해주면 최적화되지 않을까? 

그럼 0으로 이루어진 arr은 어떻게 만들지?

n * 10 +1 으로 해주면 되려나? -> 최댓값은 어차피 n * 10이기 때문.

***문제 상황: 시작값이 n*10 이면 arr의 크기또한 n*10 +1 이면 이미 최대값임
(n*10)*2 + 1 를 arr의 크기로 해주면:

0 1 2 ... n*10(x0) n*10+1 ... n*10*2 +1

아마 해결이 될 듯 하다. 즉, len(arr) -> 20n+1

-> 위 과정이 실행된 리스트를 만드는 데에는 성공했다. -> 그럼 겹치는 구간의 길이는 어떻게 구하지??

일단 arr을 단순화시키자 -> [0] 을 다 삭제하자. remove() 함수 사용.

'구간'을 칠했으니 arr에서 2이상인 점들만 세어주면 끝

2 3 2 2 1 1 1 3 3 1 1 2 2 2

1 

'''