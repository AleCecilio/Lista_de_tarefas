from .tarefa import Tarefa, TarefaImportante, TarefaRecorrente, TarefaOcasional
from db_operations import get_db_connection

# Classe Lista de Trefas, 
#   que gerenciará as pricipais 
#   funcionalidades do programa
class Lista_Tarefas:
    # Construtor 
    def __init__(self, nome_lista):
        self.nome_lista = nome_lista
        self.tarefas = []
        self._carregar_tarefas()
    