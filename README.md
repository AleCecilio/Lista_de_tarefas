# Lista_de_tarefas
Projeto 4: Lista de Tarefas Persistente (Orientação a Objetos e SQLite)
Um sistema de gerenciamento de tarefas simples e robusto, construído em Python, que utiliza Programação Orientada a Objetos (POO), modularização avançada e o banco de dados SQLite para garantir a persistência imediata dos dados após cada operação.

🚀 Funcionalidades
Funcionalidade	Descrição
Persistência SQL	O estado completo da lista é salvo e carregado automaticamente do banco de dados SQLite (tarefas.db).
Adicionar Tarefa	Permite incluir novas tarefas na "Lista Principal", classificando-as por herança como Importante, Recorrente ou Ocasional.
Manipulação Completa	Funções para listar, marcar tarefas como concluídas e deletá-las.
Iteração	A classe Lista_Tarefas implementa o método especial __iter__, permitindo percorrer a lista diretamente com loops for do Python.
Separação de Preocupações	A lógica de negócio está completamente isolada das operações de banco de dados (SELECT, INSERT, UPDATE, DELETE).
Revisita Conceitos	Excelente prática para reforçar o aprendizado de Herança, Polimorfismo, Agregação, Context Managers e Módulos de Persistência.

Exportar para as Planilhas
🛠️ Como Executar
Para rodar a aplicação, certifique-se de que você tem o Python instalado (versão 3.8+ recomendada) e que a estrutura de diretórios foi mantida.

Navegue até o diretório principal do projeto no terminal.

Crie a tabela no banco de dados (geralmente isso é feito automaticamente na primeira execução, mas garante a estrutura).

Execute o arquivo principal com o seguinte comando:

Bash

python lista_tarefas_app.py
📂 Estrutura do Projeto
O projeto é organizado em pacotes, com cada classe e módulo em seu próprio arquivo, garantindo a máxima modularidade e facilidade de manutenção.

projeto_lista_tarefas/
├── lista_tarefas_app.py    # O arquivo principal que executa o menu interativo
├── classes/                # Pacote com todas as classes de POO do projeto
│   ├── __init__.py         # Torna a pasta um pacote Python
│   ├── cls_lista.py        # Classe central que gerencia a lista (Lista_Tarefas)
│   └── tarefa.py           # Classes: Tarefa, TarefaImportante, TarefaRecorrente, etc.
├── db_operations/          # Pacote para toda a lógica de persistência (SQL)
│   ├── __init__.py         # Torna a pasta um pacote Python
│   ├── operations.py       # Funções de CRUD (INSERT, SELECT, UPDATE, DELETE)
│   └── db_connection.py    # Gerencia a conexão com SQLite (@contextmanager)
└── set_entradas/           # Pacote para funções de validação de entrada
    └── set_int.py          # (Contém verifica_Int e verifica_String)
📄 Arquivos de Persistência
O sistema utiliza os seguintes arquivos e estruturas para persistência:

tarefas.db: Um arquivo gerado pelo SQLite que armazena todas as tarefas. A tabela lista_tarefas contém as colunas necessárias para o filtro e o estado de cada item.

Módulo set_entradas: Garante que a entrada do usuário para índices de tarefas e tipos de tarefa seja sempre validada.

Observação: O projeto inclui uma função (populate_tarefas_table) para iniciar o banco de dados com 20 tarefas na "Lista Principal" na primeira execução.

💡 Próximos Incrementos (Sugestões de Melhoria)
O design atual do projeto utiliza o banco de dados para suportar uma estrutura mais complexa. Onde o projeto só gerencia a "Lista Principal", o próximo passo é desbloquear a funcionalidade completa do banco de dados, tornando o sistema escalável.

1. Multi-Usuário e Multi-Lista
Gerenciamento de Usuários: Criar uma nova tabela Usuarios e associar cada Lista a um Usuario. Isso permitiria que diferentes pessoas usassem a mesma aplicação com dados isolados.

Múltiplas Listas por Usuário: Habilitar a criação, nomeação e gestão de diferentes listas de tarefas para um mesmo usuário (ex: "Trabalho", "Pessoal", "Faculdade"). A estrutura do banco de dados atual já possui a coluna lista e está pronta para suportar esta funcionalidade.

🤝 Contribuição
Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou correções, como a implementação de múltiplos usuários ou filtros avançados, sinta-se à vontade para abrir uma issue ou enviar um pull request.