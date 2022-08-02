from cadastro import Aluno
from utils import Lista
lsitaAlunos = Lista()
class Avaliacao:
    def __init__(self, matricula, n_avaliacao, peso, altura, circcintura, circquadril, circ1, circ2, circ3, flexibilidade, qtdabdominal):
        self.matricula = matricula
        self.n_avaliacao = n_avaliacao
        self.peso = peso
        self.altura = altura
        self.circcintura = circcintura
        self.circquadril = circquadril
        self.circ1 = circ1
        self.circ2 = circ2
        self.circ3 = circ3
        self.flexibilidade = flexibilidade
        self.qtdabdominal = qtdabdominal

    def get_matricula(self):
        return self.matricula

    def percentual_gordura_homem(self, idade):
        somadc = self.circ1 + self.circ2 + self.circ3
        densC = 1.10938 - (0.0008267 * somadc) + (0.0000016 * (somadc*somadc)) - (0.0002574 * idade)
        percGC= (495 / densC) - 450
        percMC = 100 - percGC
        pimax = self.peso*0.86
        pimin = self.peso*0.80
        classificacao = ''
        if percGC < 5:
            classificacao = 'Desnutrição'
        elif percGC >= 5 and percGC < 8:
            classificacao = 'Baixo peso'
        elif percGC >= 8 and percGC < 14:
            classificacao = 'Ideal'
        elif percGC >= 14 and percGC < 20:
            classificacao = 'Saudável'
        elif percGC >= 20 and percGC < 25:
            classificacao = 'Sobrepeso'
        else:
            classificacao = 'Obeso'
        return f'Percentual de gordura atual: {percGC:.2f}%\n'\
                f'Ideal minimo: 14%\n'\
                f'Ideal máximo: 20%\n'\
                f'Peso atual: {self.peso} Kg\n'\
                f'Peso ideal mínimo: {pimin:.2f} Kg\n'\
                f'Peso ideal máximo: {pimax:.2f} Kg\n'\
                f'Percentual muscular: {percMC:.2f}%\n'\
                f'Classificação: {classificacao}\n'

    def percentual_gordura_mulher(self, idade):
        somadc = self.circ1 + self.circ2 + self.circ3
        densC = 1.0994921 - (0.0009929 * somadc) + (0.0000023 * (somadc*somadc)) - (0.0001392 * idade)
        percGC = (495 / densC) - 450
        percMC = 100 - percGC
        pimax = self.peso*0.88
        pimin = self.peso*0.82
        classificacao = ''
        if percGC < 8:
            classificacao = 'Desnutrição'
        elif percGC >= 8 and percGC < 12:
            classificacao = 'Baixo peso'
        elif percGC >= 12 and percGC < 18:
            classificacao = 'Ideal'
        elif percGC >= 18 and percGC < 24:
            classificacao = 'Saudável'
        elif percGC >= 24 and percGC < 30:
            classificacao = 'Sobrepeso'
        else:
            classificacao = 'Obeso'
        return f'Percentual de Gordura corporal: {percGC:.2f}% \n'\
                f'Ideal minimo: 12%\n'\
                f'Ideal máximo: 18%\n'\
                f'Peso atual: {self.peso} Kg\n'\
                f'Peso ideal mínimo: {pimin:.2f} Kg\n'\
                f'Peso ideal máximo: {pimax:.2f} Kg\n'\
                f'Percentual muscular: {percMC:.2f}%\n'\
                f'Classificação: {classificacao}\n'
    

    def tmb_homem(self, idade):
        tmb = 66 +(13.8*self.peso)+(5*self.altura)-(6.8*idade)
        return f'Taxa Metabolica Basal: {tmb:.2f}\n'

    def tmb_mulher(self, idade):
        tmb = 655+(9.6*self.peso)+(1.8*self.altura)-(4.7*idade)
        return f'Taxa Metabolica Basal: {tmb:.2f}\n'

    def clasrisco_homem(self):
        calc = self.circcintura/self.circquadril
        risco = ''
        if calc <= 0.95:
            risco = 'Baixo'
        elif calc > 0.95 and calc <= 1:
            risco = 'Moderado'
        else:
            risco = 'Alto'
        return f'Relação Cintura-Quadril: {calc:.2f}\n'\
                f'Risco: {risco}\n'

    def clasrisco_mulher(self):
        calc = self.circcintura/self.circquadril
        risco = ''
        if calc <= 0.8:
            risco = 'Baixo'
        elif calc > 0.8 and calc <= 0.85:
            risco = 'Moderado'
        else:
            risco = 'Alto'
        return f'Relação Cintura-Quadril: {calc:.2f}\n'\
                f'Risco: {risco}\n'

    def imc(self):
        imc = self.peso/self.altura**2
        classificacao = ''
        if imc < 18.5:
            classificacao = 'Baixo peso'
        elif imc >= 18.5 and imc < 25:
            classificacao = 'Peso adequado'
        elif imc >= 25 and imc < 30:
            classificacao = 'Sobrepeso'
        else:
            classificacao = 'Obesidade'
        return f'IMC: {imc:.2f}\n' \
                f'Classificação: {classificacao}\n'

    def __str__(self):
        return f'Aluno: {self.matricula}\nAvaliação número: {self.n_avaliacao}\nPeso: {self.peso}\nAltura: {self.altura}\nCircunferência cintura: {self.circcintura}\nCircunferência quadril: {self.circquadril}\n'\
                f'Dobra cutânea 1: {self.circ1}\nDobra cutânea 2: {self.circ2}\nDobra cutânea 3: {self.circ3}\nFlexibilidade: {self.flexibilidade}\nQuantidade Abdominal: {self.qtdabdominal}'
