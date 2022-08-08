def main():

    text = 'Welcome to Python class'

    print(text.upper())

    print(len(text))

    print(len([1,2,3,4]))

    age = 23
    name = 'Yu'

    print('Hi I am {}, {} this year'.format(name, age))
    print('Hi I am ' + name + ', ' + str(age) + ' this year')
    print(f'Hi I am {name}, {age} this year')

main()