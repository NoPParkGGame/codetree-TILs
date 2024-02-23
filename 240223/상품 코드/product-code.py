class product:
    def __init__(self, name='', code=0):
        self.name=name
        self.code=code

prod_info_A=product()

prod_info_A.name='codetree'
prod_info_A.code='50'

name, code=tuple(input().split())

prod_info_B=product(name, code)

print(f'product {prod_info_A.code} is {prod_info_A.name}')
print(f'product {prod_info_B.code} is {prod_info_B.name}')