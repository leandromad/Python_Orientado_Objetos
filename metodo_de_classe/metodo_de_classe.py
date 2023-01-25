from datetime import datetime


class Empresa:

    ano_atual = datetime.now().year #atributo de classe. Não importa a instância

    def __init__(self, nome, ticker, ano_fundacao, cnpj): # construtor

        self.nome = nome #atributos da instancia
        self.ticker = ticker
        self.ano_fundacao = ano_fundacao
        self.cnpj = cnpj
        

    def tempo_existencia(self):

        self.anos_existencia = self.ano_atual - self.ano_fundacao
        print(f"A empresa existe há {self.anos_existencia} anos!")

    def cnpj_numerico(self):

        self.cnpj_inteiro = int(self.cnpj.replace("-","").replace(".","").replace("/",""))
        print(f"O CNPJ só com números é {self.cnpj_inteiro}.")


#Classe é referente a classe, não a instância (objeto específico).
#Pode ser usado para contruisr as intâncias, quando você só tem parte dos argumentos necessários.
#Vamos supor que você precisa do ano de fundação mas só tem os anos de existência da empresa.
#Você pode construit um método de classe que calcula isso para você.

    @classmethod
    def extraindo_empresa_por_ano_existencia(cls, anos_existencia, nome, ticker, cnpj):

        ano_fundacao = cls.ano_atual - anos_existencia
        return cls(nome, ticker, ano_fundacao, cnpj) #tem que ser na mesma ordem do init

    @classmethod
    def extraindo_empresa_corrigindo_ticker(cls, nome, texto_ticker, codigo_ticker, ano_fundacao, cnpj):

        ticker = texto_ticker + codigo_ticker
        return cls(nome, ticker, ano_fundacao, cnpj) #tem que ser na mesma ordem do init


        #usado pra quando você não tem, ou não quer ter a instancia no primeiro momento

if __name__ == "__main__":

    weg = Empresa.extraindo_empresa_por_ano_existencia(nome = 'WEG', ticker = 'WEGE3', anos_existencia = 62, cnpj='84.429.695/0001-11')
    print(weg.ano_fundacao)

    weg = Empresa.extraindo_empresa_corrigindo_ticker(nome = 'WEG', texto_ticker = 'WEGE', codigo_ticker = '3', ano_fundacao=1960, cnpj ='84.429.695/0001-11')
    print(weg.ticker)