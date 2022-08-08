print('Electricity bill estimator ')
cents = int(input('Enter cents per kWh: '))
usage = float(input('Enter daily use in kWh: '))
days = int(input('Enter number of billing days: '))

price = (cents *0.01) * usage * days
print(f'Estimated bill: ${price:.2f}')