n=int(input())

class User_info:
    def __init__(self, name, height, weight):
        self.name=name
        self.height=height
        self.weight=weight

arr=[tuple(input().split()) for _ in range(n)]
users_arr=[User_info(name, height, weight) for name, height, weight in arr]

users_arr.sort(key=lambda x: x.height)

for user in users_arr:
    print(user.name, user.height, user.weight)