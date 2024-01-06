hap=0
cnt=0
while True:
    age=int(input())
    if 19<age<30:
        hap+=age
        cnt+=1
    else:
        break
print(f'{hap/cnt:.2f}')