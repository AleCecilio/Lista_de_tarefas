# Lista_de_tarefas

Projeto 4: Lista de Tarefas Persistente (Orientação a Objetos e SQLite)

Um sistema de gerenciamento de tarefas simples e robusto, construído em Python, que utiliza Programação Orientada a Objetos (POO), modularização avançada e o banco de dados SQLite para garantir a persistência dos dados após cada operação.

## 🚀 Funcionalidades

| Funcionalidade           | Descrição                                                                                   |
|-------------------------|---------------------------------------------------------------------------------------------|
| Persistência SQL        | Estado salvo e carregado automaticamente do banco SQLite (`tarefas.db`).                    |
| Adicionar Tarefa        | Inclusão de novas tarefas, classificadas por herança como Importante, Recorrente ou Ocasional.|
| Manipulação Completa    | Listar, marcar como concluída e deletar tarefas.                                            |
| Iteração                | Classe `Lista_Tarefas` implementa `__iter__`, permitindo loops `for` diretamente.           |
| Separação de Preocupações | Lógica de negócio isolada das operações de banco de dados.                                 |
| Revisita Conceitos      | Prática de Herança, Polimorfismo, Agregação, Context Managers e Módulos de Persistência.    |

## 🛠️ Como Executar

1. Certifique-se de ter Python 3.8+ instalado.
2. Navegue até o diretório principal do projeto no terminal.
3. Execute o arquivo principal:

```bash
python lista_tarefas_app.py
```

## 📂 Estrutura do Projeto

```
projeto_lista_tarefas/
├── lista_tarefas_app.py    # Menu interativo principal
├── classes/
│   ├── __init__.py
│   ├── cls_lista.py        # Classe Lista_Tarefas
│   └── tarefa.py           # Classes de tarefas
├── db_operations/
│   ├── __init__.py
│   ├── operations.py       # Funções CRUD
│   └── db_connection.py    # Conexão SQLite
└── set_entradas/
    └── set_int.py          # Validação de entrada
```

## 📄 Arquivos de Persistência

- `tarefas.db`: Banco SQLite que armazena todas as tarefas.
- Módulo `set_entradas`: Validação de índices e tipos de tarefa.

Observação: Função `populate_tarefas_table` inicia o banco com 20 tarefas na primeira execução.

## 💡 Próximos Incrementos

- **Multi-Usuário e Multi-Lista**: Nova tabela `Usuarios` e múltiplas listas por usuário.
- Estrutura pronta para escalabilidade e filtros avançados.

## 🤝 Contribuição

Contribuições são bem-vindas! Sugestões e melhorias podem ser enviadas via issue ou pull request.
