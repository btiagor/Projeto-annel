"""
    Projeto feito para demonstrar alguns habilidades em python e banco.
    Fonte de dados utilizada:
    https://dadosabertos.aneel.gov.br/dataset/siga-sistema-de-informacoes-de-geracao-da-aneel/resource/11ec447d-698d-4ab8-977f-b424d5deee6a

    Tiago Bezerra 09/02/22

"""
import csv
import codecs
import base as bs
import baixar_base as bb


def main(csv_reader):
        
    bs.create_table()

    # contador para pular cabeçalho
    count = 0
    for row in csv_reader:
        if count != 0:
            r = ''.join(row).split(';')
            # print('.', end='')
            try:
                bs.inserir(r)
            except Exception as e:
                print(e, 'linha', r)
        count += 1    


if __name__ == '__main__':
    file = 'siga-empreendimentos-geracao.csv'
    
    # pegar a base mais atualizada
    bb.baixar_base_dados()
    csv_reader = csv.reader(codecs.open(file, 'rU', 'utf-16'))
    main(csv_reader)
    