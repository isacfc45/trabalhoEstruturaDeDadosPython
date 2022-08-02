from cadastro import Aluno
from avaliação import Avaliacao
from utils import Lista, Leitor

nome_arquivo = 'aluno.txt'
listaAlunos = Lista()
listaAvaliacao = Lista()


# bd = Leitor('aluno.txt')

"""
1 - Cadastrsar Aluno
2 - Listar Alunos
3 - Realizar Avaliacação

"""



class Menu:
    def __init__(self):
        self.menu()

    def inicializar(self):
        leitor = Leitor(nome_arquivo)
        leitor.open()
        aluno = leitor.fetchRecord()
        while aluno != None:
            listaAlunos.inserir(aluno)
            aluno = leitor.fetchRecord()
        leitor.close()

    def listar_alunos(self):
        for aluno in listaAlunos:
            print(aluno)

    def busca_aluno(self):
        matricula = input("Informe a matricula: ")
        for aluno in listaAlunos:
            if aluno.get_matricula() == matricula:
                return aluno
        return None

    def busca_avaliacao(self, aluno):
        for avaliacao in listaAvaliacao:
            if avaliacao.get_matricula() == aluno.matricula:
                return avaliacao
        return None

    def resultado_avaliacao(self, aluno, avaliacao):
        print('########### Resultados ###########\n')
        if aluno.sexo == 'm':
            idade = 2022 - aluno.ano            
            print('Composição Corporal\n')
            print(avaliacao.percentual_gordura_homem(idade))
            print('Taxa metabolica\n')
            print(avaliacao.tmb_homem(idade))
            print('Classificação de risco\n')
            print(avaliacao.clasrisco_homem())
            print('IMC\n')
            print(avaliacao.imc())
        else:
            idade = 2022 - aluno.ano            
            print('Composição Corporal\n')
            print(avaliacao.percentual_gordura_mulher(idade))
            print('Taxa metabolica\n')
            print(avaliacao.tmb_mulher(idade))
            print('Classificação de risco\n')
            print(avaliacao.clasrisco_mulher())
            print('IMC\n')
            print(avaliacao.imc())


    def cadastrar_aluno(self):
        matricula = input('Matricula: ')
        # nome = str(input('Nome: '))
        sexo = str(input('Sexo: '))
        # dia = int(input('Dia: '))
        # mes = int(input('Mês: '))
        # ano = int(input('Ano: '))

        arquivo = open("aluno.txt", "a")
        # arquivo.write(aluno)


        aluno = Aluno(matricula, 'nome', sexo, 'dia', 'mes', 1995)
        listaAlunos.inserir(aluno)

        #bd.adicionar_bd(aluno)
        print('Cadastro finalizado!')


    def avaliacao(self, aluno):
        if aluno.sexo == 'm':
            # print('Informações do aluno!')
            # peso = float(input('Peso em kg: '))
            # altura = float(input('Altura em cm: '))
            # circcintura = float(input('Circunferência Cintura: '))
            # circquadril = float(input('Circunferência Quadril: '))
            # circ1 = int(input('Peitoral: '))
            # circ2 = int(input('Abdominal: '))
            # circ3 = int(input('Coxa: '))
            # flexibilidade = int(input('Flexibilidade: '))
            # qtdabdominal = int(input('Abdominal: '))

            avaliacao = Avaliacao(aluno.matricula, 1, 90, 1.9, 80, 90, 80, 80, 60, 25, 30)
            listaAvaliacao.inserir(avaliacao)
        else:
            print('Informações da aluno!\n')
            print('Antropometria\n')
            peso = float(input('Peso em kg: '))
            altura = float(input('Altura em cm: '))
            circcintura = float(input('Circunferência Cintura: '))
            circquadril = float(input('Circunferência Quadril: '))
            print('\n')
            print('Dobras Cutâneas\n')
            circ1 = int(input('Triceps: '))
            circ2 = int(input('Suprailiaca: '))
            circ3 = int(input('Coxa: '))
            print('\n')
            print('Percepção de esforço\n')
            flexibilidade = int(input('Flexibilidade: '))
            qtdabdominal = int(input('Abdominal: '))
            print('\n')

            avaliacao = Avaliacao(aluno.matricula, 1, peso, altura, circcintura, circquadril, circ1, circ2, circ3, flexibilidade, qtdabdominal)
            listaAvaliacao.inserir(avaliacao)

    def menu(self):
        self.inicializar()
        a = -1
        while True:
            print('####################################################################')
            print('######################## Avaliação Física! #########################')
            print('####################################################################\n')
            # print('********************************************************************\n')
            a = int(input('Digite:\n1 - Cadastrar aluno;\n2 - Listar alunos; \n3 - Realizar avaliação física;\n4 - Buscar aluno;\n5 - Dados da composição:\n '))
            if a == 1:
                # print('*********** Cadastro! ************\n')
                print('############ Cadastro ############\n')
                self.cadastrar_aluno()
                novo = str(input('Deseja fazer um novo cadastro s/n? \n'))
                if novo == 's':
                    self.cadastrar_aluno()
                else:
                    print('Fim !!!')    
            elif a == 2:
                print('############# Alunos #############\n')
                listaAlunos.imprimir()
            elif a == 3:
                print('####### Dados da Avaliação #######\n')
                aluno = self.busca_aluno()
                self.avaliacao(aluno)

            elif a == 4:
                print('########## Buscar Aluno ##########\n')
                aluno = self.busca_aluno()
                if aluno != None:
                    print(aluno)
                else:
                    print('Aluno não cadastrado!')
            else:
                print('##### Resultado da Avaliação #####\n')
                aluno = self.busca_aluno()
                avaliacao = self.busca_avaliacao(aluno)
                self.resultado_avaliacao(aluno, avaliacao)


menu = Menu()