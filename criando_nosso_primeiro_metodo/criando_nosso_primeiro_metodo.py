from datetime import datetime

class Empresa:

    def __init__(self, nome, ticker, ano_fundacao, cnpj): #construtor

        self.nome = nome #atributos da instância
        self.ticker = ticker
        self.ano_fundacao = ano_fundacao
        self.cnpj = cnpj
        self.ano_atual = datetime.now().year

    def tempo_existencia(self):
    #preciso passar o self pois é um método da instância. Só é possível executar ele com os atributos da instancia existindo
        self.anos_existencia = self.ano_atual - self.ano_fundacao
        print(f"A empresa exista há {self.anos_existencia} anos!")

    def cnpj_inteiro(self):

        self.cnpj_numerico = int(self.cnpj.replace("-","").replace(".","").replace("/",""))
        print(f"O CNPJ só com números é {self.cnpj_numerico}.")



if __name__ == "__main__":

    weg = Empresa(nome = 'WEG', ticker = 'WEGE3', ano_fundacao = 1960, cnpj = '84.429.695/0001-11')
    weg.tempo_existencia()
    weg.cnpj_inteiro()
