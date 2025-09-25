from sqlite3 import connect, ProgrammingError, OperationalError, IntegrityError
from contextlib import contextmanager 

@contextmanager
def get_db_connection():
    conexao = connect('db/listas_tarefas.db')
    try:
        yield conexao
    finally:
        conexao.close()
    