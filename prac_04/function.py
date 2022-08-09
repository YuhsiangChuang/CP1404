def value_change(param):
    param = 123
    print(param)

def my_function(param_list):
    param_list[0]+=777                      # mutable change on the array
    print(f'Param_list {param_list}')

def my_function2(param_list):
    param_list = [100, 200, 300]            # assignment creates anther list object
    print(f'Param_list_2 {param_list}')

def main():
    arg = 999
    value_change(arg)
    print(arg)
    print()

    my_list = [1,2,3]
    my_function(my_list)
    print(f'My_list {my_list}')

    my_function2(my_list)
    print(f'My_list_2 {my_list}')

main()