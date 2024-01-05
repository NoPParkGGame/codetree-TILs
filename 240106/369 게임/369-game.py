n=int(input())
indicator=[3,6,9]
for i in range(1,n+1):
    if i%3==0:
        print(0,end=' ')
    else:
        if 9<i<100: #ex) 86
            a=i//10 #10의자리 숫자 8
            b=i%10 # 1의자리 숫자 6
            for j in indicator:
                indi=0
                if a==j or b==j:
                    indi=1
                if indi==1:
                    print(0)
                else:
                    print(i)
                    
                
        else:
            print(i,end=' ')