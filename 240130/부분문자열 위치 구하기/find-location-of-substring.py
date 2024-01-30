string=input()
alph=input()

exists=False

for i in range(len(string)-len(alph)+1):
    if string[i:i+len(alph)]==alph:
        exists=True
        print(i)
        break
if exists==False:
    print(-1)