from db_connection import get_db_connection
from sqlite3 import ProgrammingError, OperationalError, IntegrityError


#Criando Tabela 'listas_tarefas'
def create_listas_tarefas():
    table_listas_tarefas= """
        CREATE TABLE IF NOT EXISTS listas_tarefas (
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
            cursor.execute(table_listas_tarefas)
            conexao.commit()
            print('Tabela Listas de Tarefas Criada com Sucesso')
    except ProgrammingError as e:
            print(f"Erro de sintaxe na instrução SQL: {e}")
    except OperationalError as e:
        print(f"Erro operacional: o banco de dados pode estar corrompido ou bloqueado. {e}")
    except IntegrityError as e:
        print(f"Erro de integridade: a atualização viola as regras da tabela. {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
