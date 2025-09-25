# Classe Tarefa 
class Tarefa:
    # Construtor
    def __init__(self, descricao, tipo, id=None):
        self.descricao = descricao
        self.concluida = False
        self.tipo = tipo
        self.id = id
    
    
    # Atualizar Tarefa Para Marcá-la como Comcluida
    def marcar_concluida (self):
        self.concluida = True

    
    # Exibir Tarefa
    def __str__(self):
        status = '✓' if self.concluida else ' '
        return f'[{status}] {self.descricao} ({self.tipo})'


# Sub classe De Tarefas Para Definir as Importantes 
class TarefaImportante(Tarefa):
    #Construtor 
    def __init__(self, descricao, id=None):
        super().__init__(descricao, 'Importante', id)
        
        
# Sub classe De Tarefas Para Definir as Recorrente 
class TarefaRecorrente(Tarefa):
    #Construtor 
    def __init__(self, descricao, id=None):
        super().__init__(descricao, 'Recorrente', id)
        

# Sub classe De Tarefas Para Definir as Ocasional 
class TarefaOcasional(Tarefa):
    #Construtor 
    def __init__(self, descricao, id=None):
        super().__init__(descricao, 'Ocasional', id)