name_file = open('name.txt', 'w')
name = input('What is your name? ')
while name =='':
    print('Please enter a valid name')
    name = input('What is your name? ')
print(name)
name_file.close()