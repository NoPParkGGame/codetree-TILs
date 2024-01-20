n=int(input())

cnt='A'

for i in range(n):
    for j in range(i+1):
        print(cnt,end='')
        cnt=chr(ord(cnt)+1)
        if cnt==chr(ord('Z')+1):
              cnt='A'      
    print()