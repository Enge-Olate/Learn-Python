class OpenCSV:
    def __init__(self, filename:str):
        self.filename = filename

    def read_csv(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            data = file.readlines()
        return data
    
    def extract_column_name(self):
        return self.read_csv()[0].strip().split(',')

    def extract_column_data(self, index: str):
        column_data = list()
        for line in self.read_csv():
            column_data_line = line.strip().split(',')
            column_data.append(column_data_line[index])
        column_data.pop(0)
        return column_data[:10]

csv_reader = OpenCSV('./listaLivrosInformatica.csv')
print(csv_reader.read_csv())
print("*"*100)
print(csv_reader.extract_column_name())
print(csv_reader.extract_column_data(index=3))