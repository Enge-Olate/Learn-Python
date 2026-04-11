from time import sleep
class Pessoa(object):
    def __init__(self, nome: str, idate:int, documento:str):
        self.nome = nome
        self.idate = idate
        self.documento = documento
    
    def __str__(self):
        return (
            f"Nome: {self.nome}\n"
            f"Idade: {self.idate}\n"
            f"Documento: {self.documento}"
        )
    
    def sleep(self, hours:int):
        sleep(hours)
        return f'{self.nome} dormiu por {hours} horas'        

pessoa = Pessoa('Márcio', 47, '000.000.000-00')
print(pessoa)
print(pessoa.sleep(2))

class Estudante(Pessoa):
    def __init__(self, nome: str, idate:int, documento:str, curso:str):
        super().__init__(nome, idate, documento)
        self.curso = curso
        
    def cursos(self, curso:str):
        return f'{self.nome} está matriculado no curso de {curso}'

estudante = Estudante('Márcio', 47, '000.000.000-00', 'Engenharia de Software')
print(estudante.cursos(estudante.curso))
        