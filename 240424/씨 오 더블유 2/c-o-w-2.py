n=int(input())

word=list(input())
ans=0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1,n):
            if word[i]=='C' and word[j]=='O' and word[k]=='W':
                ans+=1
print(ans)