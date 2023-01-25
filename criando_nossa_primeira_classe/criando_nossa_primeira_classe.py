class Empresa:

    def __init__(self, nome, ticker, data_de_fundacao, cnpj): #construtor

        self.nome = nome #atributos da instância
        self.ticker = ticker
        self.data_de_fundacao = data_de_fundacao
        self.cnpj = cnpj

class Carro:

    def __init__(self, cor, direcao):

        self.cor_do_carro = cor
        self.tipo_direcao = direcao

if __name__ == "__main__": #isso aqui serve para fazer testes dentro do próprio código. Só vai rodar quando rodar esse código como main

    empresa_de_motor = Empresa(nome = 'WEG', ticker = 'WEGE3', data_de_fundacao = 1960, cnpj = "138432221")
    carro_do_nelson = Carro(cor = 'Preta', direcao = 'Elétrica')

    print(empresa_de_motor.data_de_fundacao)
    print(carro_do_nelson.cor_do_carro)
