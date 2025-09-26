from db_operations import create_lista_tarefas
from classes import Lista_Tarefas
from set_entradas import verifica_Int
from sys import exit
from time import sleep

# Exibe o menu principal
def exibir_menu():
    print('\n' + '=' * 30)
    print('Menu Lista De Tarefas')
    print('=' * 30)
    print('1 - Ver Tarefas (Listar)')
    print('2 - Adicionar Nova Tarefa')
    print('3 - Concluir Tarefa')
    print('4 - Deletar Tarefa')
    print('0 - Sair')
    print('-' * 30)


def main():
    try:
        create_lista_tarefas()
        print("\nConfiguração de banco de dados concluída.")
        sleep(2.5)
    except Exception as e:
        print(f"ERRO: Não foi possível configurar o banco de dados. {e}")
        return

    nome_lista = "Lista Principal"
    minha_lista = Lista_Tarefas(nome_lista)
    
    while True:
        exibir_menu()
        
        op = verifica_Int('Escolha uma opção: ', 0, 4)
        
        match op:
            case 1:
                minha_lista.listar_tarefas()
            case 2:
                minha_lista.incluir_tarefa()
            case 3:
                minha_lista.concluir_tarefa_lista()
            case 4:
                minha_lista.deletar_tarefa()
            case 0:
                exit("\nSaindo do programa. Até logo!")
            case _:
                print("Opção inválida. Tente novamente.")
                sleep(2.5)


if __name__ == '__main__':
    main()