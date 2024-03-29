num_dev, num_infect , first_infected, num_time = tuple(map(int, input().split()))
# 개발자의수, 감염횟수, 첫번째 감염자, 몇 번의 시간이 흐르는가.

arr=[
    tuple(map(int, input().split()))       
    for _ in range(num_time)
]

arr.sort()  # 시간 순으로 정렬
arr_infected=[first_infected] #감염자들의 리스트를 정리

for time, x_dev, y_dev in arr: #몇 초, 누가, 누구에게 unpacking
    if num_infect==0:  # 감염가능횟수가 0이 되면 break
        break
    if x_dev in arr_infected and y_dev not in arr_infected:   #만약 x가 감염자 리스트에 있다면
        arr_infected.append(y_dev)  # y 또한 감염자 리스트에 추가
        num_infect-=1
    elif y_dev in arr_infected and x_dev not in arr_infected: # 또는 y가 감염자 리스트에 있다면
        arr_infected.append(y_dev)  # x 또한 감염자 리스트에 추가
        num_infect-=1

arr_dev=[
    i
    for i in range(1, num_dev+1)
]

for elem in arr_dev:
    if elem in arr_infected:
        print(1,end='')
    else:
        print(0,end='')