def main():

    in_fail = open('guitars.txt', 'r')

    lines = in_fail.readlines()
    print(lines)

    for line in lines:
        guitar_data = line.split(',')
        name = guitar_data[0]
        year = guitar_data[1]
        price = guitar_data[2]
        print(f'Guitar {name} is made in {year} and costs ${price}')

        print(f'Now Guitar {name} made in {year} is costing ${price *1/2 :.2f}')