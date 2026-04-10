import csv
file = './ListadePrecosNovatec-NOVEMBRO2025.csv'
prices = []
prices_float =[]
try:
    with open(file=file, encoding='utf-8', mode='r') as file:
        line = csv.reader(file)
        next(line)
        for row in line:
            prices_str = row[4].strip()
            prices.append(prices_str)
        
except FileNotFoundError:
    print('File not found')

print(f'Prices str: {prices[0:10]}')

for price in prices:
    if price and any(char.isdigit() for char in price):
        price_float = float(price.replace('R$', '').replace('.', '').replace(',', '.').strip())
        prices_float.append(price_float)

print(f'Prices float: {prices_float[0:10]}')



