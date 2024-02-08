n=int(input())

def sum_each(n):
    if n<10:
        return n**2
    return sum_each(n // 10) + (n % 10)**2

print(sum_each(n)) 

'''
n -> 1527
return n//10 1 + 5 + 2 + 7

(n//10) -> 152
return n//10 1+ 5 + 2

n//10 -> 15
return n//10 -> 1 + 5

n//10 => 1 -> return 1


'''