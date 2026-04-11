file = './listaLivrosInformatica.csv'
conteudo = []
try:
    with open(file=file, encoding='utf-8',mode='r') as file:
        leitor = file.readline()
        while leitor:
            conteudo.append(leitor)
            leitor = file.readline()
except FileNotFoundError:
    print('File not found')

for linha in conteudo:
    print(linha)
print(type(conteudo))