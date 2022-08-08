name = input('Enter name: ')
print('(H)ello')
print('(G)oodbye')
print('(Q)uit')
choice = input('>>> ').upper()
while choice != 'Q':
    if choice == 'H':
        print(f'Hello {name}')
        choice = input('>>> ').upper()
    elif choice == 'G':
        print(f'Goodbye {name}')
        choice = input('>>> ').upper()
    else:
        print('Invalid choice')
        choice = input('>>> ').upper()
print('Finished.')