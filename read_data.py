import pandas as pd

df = pd.read_csv('data/dow_jones_index.csv')
df.head(n=10)

df.columns.to_list()
lines, columns = df.shape
print(f'Number of lines: {lines}')
print(f'Number of columns: {columns}')

df_mcd = df[df['stock']=='MCD']
df_mcd = df_mcd[['date', 'open', 'high', 'low', 'close']]
df_mcd.head(n=10)
df_mcd.dtypes
for col in ['open', 'high', 'low', 'close']:
    df_mcd[col] = df_mcd[col].apply(lambda value: float(value.split('$')[-1]))
    
df_mcd.head(n=10)
df_mcd.dtypes
print(f"Minumum closing price: {df_mcd['close'].min()}")
print(f"Minumum closing price: {df_mcd['open'].min()}")
print(f"Maximun closing price: {df_mcd['close'].max()}")
print(f"Maximun closing price: {df_mcd['open'].max()}")