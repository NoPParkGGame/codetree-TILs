n= int(input())

mirror=[
    list(input())
    for _ in range(n)
]
laser=int(input())





'''
    1  2  3  4      range(1, n)
16              5
15              6
14              7
13              8
    12 11 10 9      range(3n, 3n-(n-1), -1)

range(1,n) 그리고 range(3n-(n-1), 3n) [수직]은 같은 입사각 반사각을 가짐.
: / 오른쪽, \ 왼쪽


range(n+1, 2n) 그리고 range(4n-(n-1) , 4n) [수평]은 같은 반사각을 가짐
: / 왼쪽, \ 오른쪽
'''