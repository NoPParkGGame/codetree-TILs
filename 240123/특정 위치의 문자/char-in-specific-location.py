arr=['L','E','B','R','O','S']
word=input()
for i,elem in enumerate(arr):
    if elem==word:
        print(i)
if word not in arr:
    print('None')