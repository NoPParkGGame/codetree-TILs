num_dev, num_infect , first_infected, num_time = tuple(map(int, input().split()))
# 개발자의수, 감염횟수, 첫번째 감염자, 몇 번의 시간이 흐르는가.

arr=[
    tuple(map(int, input().split()))       
    for _ in range(num_time)
]
arr_num_infect=[0] + [num_infect]*num_dev   # 각 개발자들의 감염 횟수를 따로 관리해 주어야 함.

arr.sort()  # 시간 순으로 정렬
arr_infected=[first_infected] #감염자들의 리스트를 정리

for time, x_dev, y_dev in arr: #몇 초, 누가, 누구에게 unpacking

    if (x_dev in arr_infected and arr_num_infect[x_dev]>0) and (y_dev in arr_infected and arr_num_infect[y_dev]>0):
        arr_num_infect[x_dev]-=1
        arr_num_infect[y_dev]-=1    # 둘 다 감염자라면 감염가능횟수만 -1

    elif x_dev in arr_infected and arr_num_infect[x_dev]>0 :   #만약 x가 감염자 리스트에 있고 감염횟수가 0이 아니라면        
        arr_infected.append(y_dev)  # y 또한 감염자 리스트에 추가
        arr_num_infect[x_dev]-=1    # x의 감염횟수 감소
        
    elif y_dev in arr_infected and arr_num_infect[y_dev]>0: # 또는 y가 감염자 리스트에 있고 감염횟수가 0이 아니라면
        arr_infected.append(x_dev)  # x 또한 감염자 리스트에 추가
        arr_num_infect[y_dev]-=1    # y의 감염횟수 감소
    


arr_dev=[
    i
    for i in range(1, num_dev+1)
]

for elem in arr_dev:
    if elem in set(arr_infected):
        print(1,end='')
    else:
        print(0,end='')