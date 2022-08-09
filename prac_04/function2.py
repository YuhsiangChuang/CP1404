def fin(arg1 =[], arg2 = 27):
    arg1.append(arg2)
    return arg1

my_list = [1,2,3]
print(fin(my_list, 4))
print(fin(my_list))
print(fin())
print(fin())
print(fin())