# -*- coding: utf-8 -*-

import sqlite3
name_db = 'BaseEstudoAneel.db'
name_tb = 'aneel'

# Função que abre a conexão
def open_conection(db=name_db):
    conn = sqlite3.connect(db)
    return conn


# Função que fecha a conexão
def close_conection(conn):
    conn.close()

    
# Função para criar tabela principal do banco.
def create_table():    
    my_conn = open_conection()
    if crud(f'SELECT NAME FROM SQLITE_MASTER WHERE TYPE = "table" AND NAME = "{name_tb}"'):        
        print('TABELA JÁ EXISTE.')
    else:        
        my_conn.execute(
            f"""                    
            CREATE TABLE {name_tb} (
                ANE_Id INTEGER PRIMARY KEY,
                ANE_DatGeracaoConjuntoDados TEXT,
                ANE_IdcGeracaoQualificada TEXT,
                ANE_NomEmpreendimento TEXT,
                ANE_CodCEG TEXT,
                ANE_SigUFPrincipal TEXT,
                ANE_DscAbreviacaoTipoGeracao TEXT,
                ANE_DscFaseUsina TEXT,
                ANE_DscOrigemCombustivel TEXT,
                ANE_DscFonteCombustivel TEXT,
                ANE_DscTipoOutorga TEXT,
                ANE_NomFonteCombustivel TEXT,
                ANE_DatEntradaOperacao  TEXT,
                ANE_MdaPotenciaOutorgadaKw INTEGER,
                ANE_MdaPotenciaFinalizadaKw INTEGER,
                ANE_MdaGarantiaFisicaKw INTEGER,
                ANE_NumLatitude TEXT,
                ANE_NumLongitude TEXT,
                ANE_DatInicioVigencia  TEXT,
                ANE_DatFimVigencia  TEXT,
                ANE_DscPropriRegimePariticipacao TEXT,
                ANE_DscSubBacia TEXT,
                ANE_DscMuninicpios TEXT              
                )
            """
            )
        print('TABELA CRIADA!!!')        
    close_conection(my_conn)

# Função utilizada para Criar - Ler - Atualizar - Deletar na base
def crud(query, db=name_db):
    my_conn = open_conection(db)
    
    if 'select' in query.lower():
        resp = my_conn.execute(query)
        resp = [x for x in resp]
        close_conection(my_conn)
        return resp
    else:
        my_conn.execute(query)
        my_conn.commit()
    close_conection(my_conn)


def inserir(array):

    query = f"""select * from {name_tb} where 
            ANE_DatGeracaoConjuntoDados = '{array[0]}' and
            ANE_IdcGeracaoQualificada = '{array[1]}' and
            ANE_NomEmpreendimento = '{array[2]}' and
            ANE_CodCEG = '{array[3]}' and
            ANE_SigUFPrincipal = '{array[4]}' and
            ANE_DscAbreviacaoTipoGeracao = '{array[5]}' and
            ANE_DscFaseUsina = '{array[6]}' and
            ANE_DscOrigemCombustivel = '{array[7]}' and
            ANE_DscFonteCombustivel = '{array[8]}' and
            ANE_DscTipoOutorga = '{array[9]}' and
            ANE_NomFonteCombustivel = '{array[10]}' and
            ANE_DatEntradaOperacao = '{array[11]}' and
            ANE_MdaPotenciaOutorgadaKw = '{array[12]}' and
            ANE_MdaPotenciaFinalizadaKw = '{array[13]}' and
            ANE_MdaGarantiaFisicaKw = '{array[14]}' and
            ANE_NumLatitude = '{array[15]}' and
            ANE_NumLongitude = '{array[16]}' and
            ANE_DatInicioVigencia = '{array[17]}' and
            ANE_DatFimVigencia  = '{array[17]}' and
            ANE_DscPropriRegimePariticipacao = '{array[19]}' and
            ANE_DscSubBacia = '{array[20]}' and
            ANE_DscMuninicpios = '{array[21]}'
    """
    f = crud(query)
    if not f:
        crud(            
        f"""insert into {name_tb} 
        (ANE_DatGeracaoConjuntoDados, ANE_IdcGeracaoQualificada, ANE_NomEmpreendimento, ANE_CodCEG, ANE_SigUFPrincipal, ANE_DscAbreviacaoTipoGeracao,
        ANE_DscFaseUsina, ANE_DscOrigemCombustivel, ANE_DscFonteCombustivel, ANE_DscTipoOutorga, ANE_NomFonteCombustivel, ANE_DatEntradaOperacao ,
        ANE_MdaPotenciaOutorgadaKw, ANE_MdaPotenciaFinalizadaKw, ANE_MdaGarantiaFisicaKw, ANE_NumLatitude, ANE_NumLongitude, ANE_DatInicioVigencia ,
        ANE_DatFimVigencia , ANE_DscPropriRegimePariticipacao, ANE_DscSubBacia, ANE_DscMuninicpios) 
        values ("{array[0]}","{array[1]}","{array[2]}","{array[3]}","{array[4]}","{array[5]}","{array[6]}","{array[7]}","{array[8]}",
        "{array[9]}","{array[10]}","{array[11]}","{array[12]}","{array[13]}","{array[14]}","{array[15]}","{array[16]}","{array[17]}","{array[18]}",
        "{array[19]}","{array[20]}","{array[21]}")
        """)
