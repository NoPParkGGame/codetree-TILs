string_A = list(input())
string_B= list(input())

while ''.join(string_B) in ''.join(string_A):
    for i in range(len(string_A)-len(string_B)):  #0 부터 4까지 돌거임 5 이상 index out
        if string_A[i:i+len(string_B)]==string_B:
            string_A=''.join(string_A)
            string_A= string_A[:i]+string_A[i+len(string_B):]
            string_A=list(string_A)
            
print(''.join(string_A))
'''

2   3
01  456

2
'''