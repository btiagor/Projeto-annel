from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from time import sleep
import re
import os

logs = 'baixado no dia.csv'
arquivo = 'C:/Users/leaodonorte/Downloads/siga-empreendimentos-geracao.csv'

def tratar_data(data):
    """
        Função para tratar a data obtida do site
    """    
    dict_mes = {
    'janeiro':'1', 'fevereiro':'2', 'março':'3', 'abril':'4', 'maio':'5', 'junho':'6', 'julho':'7', 
    'agosto':'8', 'setembro':'9', 'outubro':'10', 'novembro':'11', 'dezembro':'12'
    }
    dt = data.split(' ')    
    new_dt = []
    for x in dt:
        if x in dict_mes:
            new_dt.append(dict_mes[x])
        else:
            new_dt.append(x)

    new_dt = '/'.join(new_dt)
    return datetime.strptime(new_dt, '%d/%m/%Y').strftime('%d/%m/%Y')


def atualizar_data(base, data):
    """
        Função para atualizar csv de datas        
    """
    try:            
        str = ''
        with open(logs) as f:
            for i in f:        
                l = i.split(';')
                if l[0] == base:
                    str += f'{base};{data}\n'
                else:
                    str += i
        with open(logs, 'w') as f:
            f.write(str)
    
    except:        
        with open(logs, 'w') as f:
            f.write(f'{base};{data}\n')  


def validar_data(base, data):
    """
        Função que compara data da ultima atualização com a atual.
        atual > antiga - > True
        CC - > False
    """
    with open(logs) as f:
        for i in f:        
            l = i.split(';')
            if l[0] == base:
                print(f'achei {l[0]}')
                print(l[1][:-1], data.strip())
                dt_antiga = datetime.strptime(l[1][:-1], '%d/%m/%Y').date()
                dt_nova = datetime.strptime(data, '%d/%m/%Y').date()
                if dt_antiga < dt_nova:
                    return True
                else:
                    return False
        
def aguarda_download(arquivo):
    while True:
        arq = os.path.isfile(arquivo)
        if arq:
            break
        else:
            print('.', end='')
            sleep(0.5)

    
def baixar_base_dados():
        
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    browser = Chrome(ChromeDriverManager().install(), options=chrome_options)
    browser.maximize_window()
    browser.implicitly_wait(10) # seconds

    url = 'https://dadosabertos.aneel.gov.br/dataset/siga-sistema-de-informacoes-de-geracao-da-aneel/resource/11ec447d-698d-4ab8-977f-b424d5deee6a'
    browser.get(url)

    # obter data da última atualização da base
    t = browser.find_elements_by_tag_name('tbody')
    for x in t:
        if 'Dados atualizados pela última vez' in x.text:
            data_tratada = tratar_data(re.search('(\d{1,2} de \w* de \d{4})', x.text).group().replace('de', '').replace('  ', ' '))

    # se data da última atualização for menor que atual baixa ou caso não exista registro de download
    if os.path.isfile(f'./{logs}'):
        if validar_data('aneel', data_tratada):
            browser.find_element_by_xpath('//*[contains(text(), "URL: ")]/a').click()
            aguarda_download(arquivo)
        
        atualizar_data('aneel', datetime.now().strftime('%d/%m/%Y'))
        browser.close()
    else:
        browser.find_element_by_xpath('//*[contains(text(), "URL: ")]/a').click()
        aguarda_download(arquivo)
        atualizar_data('aneel', datetime.now().strftime('%d/%m/%Y'))
        browser.close()
