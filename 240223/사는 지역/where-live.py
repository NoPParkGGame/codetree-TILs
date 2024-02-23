n=int(input())

class User_info:
    def __init__(self, name, address, region):
        self.name=name
        self.address=address
        self.region=region
arr=[]
for _ in range(n):
    name, address, region= tuple(input().split())
    arr.append(User_info(name, address, region))
name_arr=[]
for i in range(n):
    name_arr.append(arr[i].name)
name_arr=sorted(name_arr, reverse=True)

for i in range(n):
    if name_arr[0] == arr[i].name:
        print(f'name {arr[i].name}')
        print(f'addr {arr[i].address}')
        print(f'city {arr[i].region}')