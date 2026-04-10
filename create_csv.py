import csv
file = './ListadePrecosNovatec-NOVEMBRO2025.csv'
prices = []
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

try:
    with open('prices.csv', mode='w', encoding='utf-8') as fp:
        line = 'Price\n'
        fp.write(line)
        for price in prices[0:10]:
            line = str(price)+'\n'
            fp.write(line)
except Exception as e:
    print(f'An error occurred while writing to the file: {e}')
    

try:
    with open('prices.csv', mode='a', encoding='utf-8') as fp:
        for price in prices[11:20]:
            line = str(price)+'\n'
            fp.write(line)
except Exception as e:
    print(f'An error occurred while writing to the file: {e}')