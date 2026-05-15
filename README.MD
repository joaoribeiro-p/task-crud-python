# CRUD de Tarefas

Aplicação web de gerenciamento de tarefas desenvolvida em Python utilizando Flask e SQLite.
O projeto foi estruturado em camadas para separar responsabilidades
e facilitar manutenção da aplicação.

## Tecnologias

- Python
- SQLite
- Flask
- HTML/CSS

## Funcionalidades

- Criar tarefas
- Listar tarefas
- Editar tarefas
- Deletar tarefas
- Concluir tarefas
- Re-abrir tarefas já concluidas


## Estrutura do Projeto

```bash
TASK-CRUD-PYTHON/
├── app/
│   ├── models/
│   │   ├── __init__.py
│   │   └── taskmodel.py
│   ├── routes/
│   │   └── rotas.py
│   ├── services/
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── templates/
│   │   ├── edit.html
│   │   └── index.html
│   ├── __init__.py
│   ├── database.py
│   └── main.py
├── instance/
├── .gitignore
├── README.md
└── run.py
```

## Arquitetura

- `routes`: recebe as requisições e retorna as respostas.
- `models`: representa as entidades.
- `services`: concentra regras de negócio.
- `templates`: contém as páginas HTML.
- `static`: armazena arquivos públicos como CSS.


## Como executar

Clone o repositório:

```bash
git clone <url-do-repo>
cd TASK-CRUD-PYTHON
```

Crie e ative o ambiente virtual:

```bash
python -m venv venv
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o projeto:

```bash
python run.py
```