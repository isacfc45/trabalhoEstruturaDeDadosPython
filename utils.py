# from pathlib import Path
from cadastro import Aluno

class Leitor:
    """
    Recebe como parametro o nome do arquivo
    """
    def __init__(self, input_src):
        self._inputSrc = input_src
        self._inputFile = None

    def open(self):
        self._inputFile = open(self._inputSrc, "r", encoding="UTF-8")

    # def adc_arquivo(self):
    #     self._inputFile = open(self._inputSrc, "a", encoding="UTF-8")

    def close(self):
        self._inputFile.close()
        self._inputFile = None

    def fetchAll(self):
        pass
    
    # def adicionarLista(self):
    #     matricula = self._inputFile.writelines()
    #     if matricula == '':
    #         return None
    #     nome = self._inputFile.writelines()
    #     sexo = self._inputFile.writelines()
    #     dia = self._inputFile.writelines()
    #     mes = self._inputFile.writelines()
    #     ano = self._inputFile.writelines()
    
    def fetchRecord(self):
        matricula = self._inputFile.readline()
        if matricula == '':
            return None
        nome = self._inputFile.readline()
        sexo = self._inputFile.readline()
        dia = self._inputFile.readline()
        mes = self._inputFile.readline()
        ano = self._inputFile.readline()
        # peso = self._inputFile.readline()
        # altura = self._inputFile.readline()
        # circcintura = self._inputFile.readline()
        # circquadril = self._inputFile.readline()
        # circ1 = self._inputFile.readline()
        # circ2 = self._inputFile.readline()
        # circ3 = self._inputFile.readline()
        # flexibilidade = self._inputFile.readline()
        # qtdabdominal = self._inputFile.readline()

        aluno = Aluno(matricula,nome, sexo, dia, mes, ano)
        
        return aluno

# peso, altura, circcintura, circquadril, circ1, circ2, circ3, flexibilidade, qtdabdominal




    # def __init__(self, nome_arq):
    #     self.nome_arq = nome_arq
    #     self.path = Path(nome_arq)

    #     if not self.path.exists() or self.path.read_text() == '':
    #         self.path.write_text('')
    
    # def adicionar_bd(self, dado):
    #     self.path.write_text(dado)

##########################################################################

# class No:
#     def __init__(self,dado):
#         self.dado = dado
#         self.proximo = None

#     def __str__(self):
#         return str(self.dado)

class Lista:
    def __init__(self):
        self.tamanho = 10
        self.elemento = [None]*self.tamanho
        self.qtd = 0

    def inserir(self,elemento):
        if self.qtd >= 10:
            print('Erro! tamanho do vetor insuficiente')
        else:
            self.elemento[self.qtd] = elemento
            self.qtd+=1

    def remover(self,posicao):
        if posicao == len(self.elemento)-1:
            self.qtd-=1
        else:
            for i in range(posicao, self.qtd):
                self.elemento[i] = self.elemento[i+1]
            self.qtd-=1

    def substituir(self, posicao, elemento):
        if posicao >= self.qtd or posicao < 0:
            print('Posição nao existe!')
        else:
            self.elemento[posicao] = elemento

    def pesquisar(self, posicao):
        if posicao >= self.qtd or posicao < 0:
            print('Posição nao existe!')
        else:
            return self.elemento[posicao]

    def imprimir(self):
        for i in range(self.qtd):
            print(self.elemento[i], end= '\n')
        print()

    def __iter__(self):
        return _BagIterator(self.elemento)

class _BagIterator:
    def __init__(self, list):
        self.bagItens = list
        self.current = 0

    def __inter__(self):
        return self

    def __next__(self):
        if self.current < len(self.bagItens):
            item = self.bagItens[self.current]
            self.current = self.current+1
            return item
        else:
            raise StopIteration

listaAluno = Lista()