h1=input().split()
h2=input().split()
h1_age, h1_gen=int(h1[0]), h1[1]
h2_age, h2_gen=int(h2[0]), h2[1]

if (h1_age>=19 and h1_gen=='M') or (h2_age>=19 and h2_gen=='M'):
    print(1)
else:
    print(0)