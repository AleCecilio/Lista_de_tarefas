from .db_connection import get_db_connection
from sqlite3 import ProgrammingError, OperationalError, IntegrityError

# Povoar a Lista
def populate_tarefas_table():
    """Insere um conjunto grande de 20 tarefas na 'Lista Principal'."""
    
    sql = """
        INSERT INTO lista_tarefas (lista, descricao, tipo, concluida)
        VALUES (?, ?, ?, ?)
    """

    tarefas_iniciais = [
        ("Lista Principal", "Revisar documentação da API", "Importante", 0),
        ("Lista Principal", "Implementar método DELETE da classe Lista", "Importante", 0),
        ("Lista Principal", "Checar e-mails da manhã", "Recorrente", 0),
        ("Lista Principal", "Comprar novo caderno", "Ocasional", 0),
        ("Lista Principal", "Pagar fatura do cartão", "Recorrente", 1), 
        ("Lista Principal", "Ler o capítulo 14 do livro de POO", "Importante", 0),
        ("Lista Principal", "Preparar slides para a próxima aula", "Importante", 1),
        ("Lista Principal", "Limpar a caixa de entrada (inbox zero)", "Recorrente", 0),
        ("Lista Principal", "Agendar manutenção do computador", "Ocasional", 0),
        ("Lista Principal", "Fazer backup dos arquivos de trabalho", "Recorrente", 0),
        ("Lista Principal", "Revisar as funções do módulo db_operations", "Importante", 0),
        ("Lista Principal", "Finalizar o Readme do projeto", "Importante", 1),
        ("Lista Principal", "Ligar para o suporte técnico", "Ocasional", 0),
        ("Lista Principal", "Responder mensagens pendentes no WhatsApp", "Ocasional", 0),
        ("Lista Principal", "Elaborar plano de estudos para a semana", "Importante", 0),
        ("Lista Principal", "Aprovar pull requests pendentes", "Recorrente", 0),
        ("Lista Principal", "Testar todas as funcionalidades do CRUD", "Importante", 0),
        ("Lista Principal", "Comprar café e filtro", "Ocasional", 1),
        ("Lista Principal", "Postar atualização do projeto no GitHub", "Ocasional", 0),
        ("Lista Principal", "Verificar logs de erro da aplicação", "Recorrente", 0),
    ]
    
    try:
        with get_db_connection() as conexao:
            cursor = conexao.cursor()
            cursor.executemany(sql, tarefas_iniciais)
            conexao.commit()
            print('\nTabela populada com 20 tarefas iniciais na "Lista Principal" com sucesso.')
            
    except ProgrammingError as e:
        print(f"Erro de sintaxe na instrução SQL: {e}")
    except OperationalError as e:
        print(f"Erro operacional: {e}")
    except IntegrityError as e:
        print(f"Erro de integridade: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Executando
if __name__ == '__main__':
    populate_tarefas_table()