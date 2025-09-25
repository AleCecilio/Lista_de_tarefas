"""
Projeto 4 - “Lista de Tarefas Persistente” (orientação a objetos)
    Criar um programa que gerencie tarefas:
    Adicionar, remover, marcar como concluída.
    Salvar automaticamente em JSON.
    Implementar iteração (método __iter__) para percorrer as tarefas.
"""
from db_operations import create_listas_tarefas


if __name__ == '__main__':
    create_listas_tarefas()