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
                if a==j or b==j:
                    print(0,end=' ')
                    pass
                else:
                    print(i,end=' ')
                    pass
        elif 99<i<370: #ex) 246
            a=i//100 #100의자리 숫자 2
            b= (i-a*100)//10 #10자리 숫자, (246-200)=> 46 //10 ->4
            c= (i-a*100)%10 # 1의자리 숫자 6
            for j in indicator:
                if a==j or b==j or c==j:
                    print(0,end=' ')
                    pass
                else:
                    print(i,end=' ')
                    pass
        else:
            print(i,end=' ')
            pass