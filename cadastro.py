# from __future__ import annotations
# # from utils import Lista, Leitor
class Aluno:
    def __init__(self,matricula, nome, sexo, dia, mes, ano):
        self.matricula = matricula
        self.nome = nome
        self.sexo = sexo
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def get_matricula(self):
        return self.matricula
        
    def alterar_nome(self, nome):
        self.nome = nome

    # def adiciona_avaliacao(self, avaliacao):
    #     self.adiciona_avaliacao(avaliacao)

    # def datadenascimento(self,dia, mes, ano):
    #     self.dia = dia
    #     self.mes = mes
    #     self.ano = ano
    #     return f'{dia}/{mes}/{ano}'
    
    def __str__(self):
        return f'Matricula: {self.matricula}\nNome: {self.nome}\nSexo: {self.sexo}\nData de nascimento: {self.dia}/{self.mes}/{self.ano}\n'                

#aluno1=Aluno()
#aluno1.matricula
#print(aluno1)