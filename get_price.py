import csv
file = './listaLivrosInformatica.csv'
columns = list()
prices_float =[]
try:
    with open(file=file, encoding='utf-8', mode='r') as file:
        line = csv.reader(file)
        next(line)
        columns.append(next(line))
except FileNotFoundError:
    print('File not found')

print(f'columns: {columns}')

# for price in prices:
#     if price and any(char.isdigit() for char in price):
#         price_float = float(price.replace('R$', '').replace('.', '').replace(',', '.').strip())
#         prices_float.append(price_float)

# print(f'Prices float: {prices_float[0:10]}')



