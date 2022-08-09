date_input = input('Enter DOB (dd/mm/yyyy) : ')
parts = date_input.split('/')
my_dob = (int(parts[0]), int(parts[1]), int(parts[2]))
print(my_dob)

date_input = input('Enter DOB (dd/mm/yyyy) : ')
parts = date_input.split('/')
my_dob = tuple([int(part) for part in parts])
print(my_dob)