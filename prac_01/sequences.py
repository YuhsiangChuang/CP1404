x= int(input('number 1: '))
y= int(input('number 2: '))
def even():
    if x % 2 == 0 :
        for i in range(x, y+1, 2):
            print(i, end=' ')
        print()
    else:
        for i in range(x+1, y+1, 2):
            print(i, end=' ')
        print()

def odd():
    if x % 2 == 0 :
        for i in range(x+1, y+1, 2):
            print(i, end=' ')
        print()
    else:
        for i in range(x, y+1, 2):
            print(i, end=' ')
        print()

def square():
    for i in range(x, y + 1, 2):
        print(i*i, end=' ')
    print()
print('**************')
even()
print('**************')
odd()
print('**************')
square()
