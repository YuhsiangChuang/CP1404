number = int(input('Number of items: '))
total_price=0
DISCOUNT=0.1

for i in range(number):
    price = float(input('Price of item: '))
    total_price+=price
if total_price > 100:
    print(f'Total price for {number} items is ${total_price * (1-DISCOUNT):.2f}')
else:
    print(f'Total price for {number} items is ${total_price}')