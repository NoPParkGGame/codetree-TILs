string, q = input().split()
q=int(q)
string=list(string)

for _ in range(q):
    arr = input().split()
    n, a, b = int(arr[0]), arr[1], arr[2]
    if n==1:
        a, b = int(a), int(b)
        string[a-1], string[b-1] = string[b-1], string[a-1]
        print(''.join(string))
    else:
        for i in range(len(string)):
            if string[i]==a:
                string[i]=b
        print(''.join(string))