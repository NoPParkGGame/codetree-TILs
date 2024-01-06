while True:
    arr=input().split()
    wid, hei, word=int(arr[0]),int(arr[1]),arr[2]
    print(wid*hei)    
    if word=='C':
        break