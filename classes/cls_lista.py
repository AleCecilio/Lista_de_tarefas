from .tarefa import Tarefa, TarefaImportante, TarefaRecorrente, TarefaOcasional
from db_operations import add_tarefa, update_tarefa_concluida, delete_tarefa, select_all_tarefas
from set_entradas import verifica_String, verifica_Int
from time import sleep

# Classe Lista de Tarefas, 
#   que gerenciará as pricipais 
#   funcionalidades do programa
class Lista_Tarefas:
    # Construtor 
    def __init__(self, nome_lista):
        self.nome_lista = nome_lista
        self.tarefas = []
        self._carregar_tarefas()
    
    
    # Iterador
    def __iter__(self):
        return iter(self.tarefas)
    
    
    # Carregar Tarefas do Banco De Dados
    def _carregar_tarefas(self):
        resultado_db = select_all_tarefas(self.nome_lista)
        
        for id, descricao, tipo, concluida in resultado_db:
            if tipo == 'Importante':
                tarefa = TarefaImportante(descricao, id)
            elif tipo == 'Recorrente':
                tarefa = TarefaRecorrente(descricao, id)
            elif tipo == 'Ocasional':
                tarefa = TarefaOcasional(descricao, id)
            else:
                tarefa = Tarefa(descricao, tipo, id)
        
            tarefa.concluida = bool(concluida)
            self.tarefas.append(tarefa)
            
    
    # Inclir nova Tarefa a Lista
    def incluir_tarefa(self):
        print('\n' + '-'*25)
        print('Incluir Nova Tarefa')
        print('-'*25)
        descricao = verifica_String('Descrição da Tarefa: ')
        
        print('Tipo da Tarefa')
        print('0) Geral')
        print('1) Importante')
        print('2) Recorrente')
        print('3) Ocasional')
        op = verifica_Int('Digite o Número da sua Opção: ', 0, 3)
        match op:
            case 0:
                tarefa = Tarefa(descricao, 'Geral')
            case 1:
                tarefa = TarefaImportante(descricao)
            case 2:
                tarefa = TarefaRecorrente(descricao)
            case 3:
                tarefa = TarefaOcasional(descricao)
                
        tarefa.id = add_tarefa(self.nome_lista, tarefa.descricao, tarefa.tipo)
        self.tarefas.append(tarefa)
        sleep(2.5)
        
    
    # Concluir tarefa
    def concluir_tarefa_lista(self):
        print('\n' + '-'*25)
        print('Concluir Tarefa')
        print('-'*25)
        
        self.listar_tarefas()
        indice = verifica_Int('Digite o Índice da Tarefa: ',0, len(self.tarefas))
        tarefa = self.tarefas[indice]
        tarefa.marcar_concluida()
        update_tarefa_concluida(tarefa.id, tarefa.concluida)
        sleep(2.5)
        
    
    # Deleta Tarefa da Lista
    def deletar_tarefa(self):
        print('\n' + '-'*25)
        print('Deletar Tarefa')
        print('-'*25)
        
        self.listar_tarefas()
        indice = verifica_Int('Digite o Índice da Tarefa: ',0, len(self.tarefas))
        tarefa = self.tarefas.pop(indice)
        delete_tarefa(tarefa.id)
        sleep(2.5)

    
    # Lista as tarefas 
    def listar_tarefas(self):
        if not self.tarefas:
            print(f"A lista '{self.nome_lista}' não tem tarefas.")
            return
        
        for i, tarefa in enumerate(self.tarefas):
            print(f"[{i}] {tarefa}")
    
        sleep(2.5)
