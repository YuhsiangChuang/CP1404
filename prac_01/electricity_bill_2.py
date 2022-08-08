TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print('Electricity bill estimator 2.0')
tariff = int(input('Which tariff? 11 or 31: '))
while tariff != 11 and tariff != 31:
    print('Invalid choice')
    tariff = int(input('Which tariff? 11 or 31: '))
usage = float(input('Enter daily use in kWh: '))
days = int(input('Enter number of billing days: '))

if tariff == 11:
    tariff = TARIFF_11
else:
    tariff = TARIFF_31

price = tariff * usage * days
print(f'Estimated bill: ${price:.2f}')