numbers = [3, 1, 4, 1, 5, 9, 2]
print(f'{numbers[0]}')              # 3
print(f'{numbers[-1]}')             # 2
print(f'{numbers[3]}')              # 1
print(f'{numbers[:-1]}')            # [3, 1, 4, 1, 5, 9]
print(f'{numbers[3:4]}')            # [1]
print(f'{5 in numbers}')            # True
print(f'{7 in numbers}')            # False
print(f'{"3" in numbers}')          # False
print(f'{numbers + [6, 5, 3]}')     # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print('_______________________')
numbers[0]= 'ten'
print(F'Answer for Q1: {numbers}')
numbers[-1]= 1
print(F'Answer for Q2: {numbers}')
print(F'Answer for Q3: {numbers[2:]}')
print(F'Answer for Q4: {9 in numbers}')
