for i in range(1, 21, 2):
    print(i, end=' ')
print()
print('*********************')

for a in range(0, 101, 10):
    print(a, end=' ')
print()
print('*********************')

for b in range(20,0,-1):
    print(b, end=' ')
print()
print('*********************')

number=int(input('Number of stars: '))
for c in range(number):
    print('*', end='')
print()
print('*********************')
number=int(input('Number of stars: '))
for d in range(number):
    print('*'*(d+1))
print()
print('*********************')