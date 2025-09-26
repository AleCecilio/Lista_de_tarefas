from .db_connection import get_db_connection
from sqlite3 import ProgrammingError, OperationalError, IntegrityError


#Criando Tabela 'listas_tarefas'
def create_lista_tarefas():
    table_lista_tarefas= """
        CREATE TABLE IF NOT EXISTS lista_tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lista TEXT,
            descricao TEXT,
            tipo TEXT,
            concluida INTEGER
        )
    """
    
    try:
        with get_db_connection() as conexao:
            cursor = conexao.cursor()
            cursor.execute(table_lista_tarefas)
            conexao.commit()
            print('Tabela Listas de Tarefas Criada com Sucesso!')
    except ProgrammingError as e:
            print(f"Erro de sintaxe na instrução SQL: {e}")
    except OperationalError as e:
        print(f"Erro operacional: o banco de dados pode estar corrompido ou bloqueado. {e}")
    except IntegrityError as e:
        print(f"Erro de integridade: a atualização viola as regras da tabela. {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


# Selecionar Dados e os retornar para classe
def select_all_tarefas(lista_nome):
    sql = """
        SELECT id, descricao, tipo, concluida 
        FROM lista_tarefas 
        WHERE lista = ?
    """

    try:
        with get_db_connection() as conexao:
            cursor = conexao.cursor()
            cursor.execute(sql, (lista_nome,))
            return cursor.fetchall()
    except ProgrammingError as e:
            print(f"Erro de sintaxe na instrução SQL: {e}")
            return []
    except OperationalError as e:
        print(f"Erro operacional: o banco de dados pode estar corrompido ou bloqueado. {e}")
        return []
    except IntegrityError as e:
        print(f"Erro de integridade: a atualização viola as regras da tabela. {e}")
        return []
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return []
    


# Adiciona Tarefa a Lista 
def add_tarefa(lista_nome, descricao, tipo):
    sql = """
        INSERT INTO lista_tarefas (lista, descricao, tipo, concluida)
        VALUES (?, ?, ?, ?)
    """ 

    
    try:
        with get_db_connection() as conexao:
            cursor = conexao.cursor()
            cursor.execute(sql, (lista_nome, descricao, tipo , 0))
            conexao.commit()
            print('Tarefa Criada com Sucesso!')
            return cursor.lastrowid
    except ProgrammingError as e:
            print(f"Erro de sintaxe na instrução SQL: {e}")
    except OperationalError as e:
        print(f"Erro operacional: o banco de dados pode estar corrompido ou bloqueado. {e}")
    except IntegrityError as e:
        print(f"Erro de integridade: a atualização viola as regras da tabela. {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    

# Update para marcar tarefa como concluída
def update_tarefa_concluida(lista_id, status):
    sql = """
        UPDATE lista_tarefas
        SET concluida = ?
        WHERE id = ?
    """
    
    try:
        with get_db_connection() as conexao:
            cursor = conexao.cursor()
            cursor.execute(sql,(int(status),lista_id))
            conexao.commit()
            print('Tarefa Concluida!')
    except ProgrammingError as e:
            print(f"Erro de sintaxe na instrução SQL: {e}")
    except OperationalError as e:
        print(f"Erro operacional: o banco de dados pode estar corrompido ou bloqueado. {e}")
    except IntegrityError as e:
        print(f"Erro de integridade: a atualização viola as regras da tabela. {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        

# Excluir Tarefa 
def delete_tarefa(tarefa_id): 
    sql = """
        DELETE FROM lista_tarefas
        WHERE id = ?
    """
    
    try:
        with get_db_connection() as conexao:
            cursor = conexao.cursor()
            cursor.execute(sql,(tarefa_id,))
            conexao.commit()
            print('Tarefa Excluída!')
    except ProgrammingError as e:
            print(f"Erro de sintaxe na instrução SQL: {e}")
    except OperationalError as e:
        print(f"Erro operacional: o banco de dados pode estar corrompido ou bloqueado. {e}")
    except IntegrityError as e:
        print(f"Erro de integridade: a atualização viola as regras da tabela. {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
