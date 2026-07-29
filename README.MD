# CRUD de Tarefas

Aplicação web para gerenciamento de tarefas, desenvolvida com Python, Flask e SQLite.

O projeto permite criar, visualizar, editar, concluir, reabrir e excluir tarefas. A aplicação também implementa exclusão lógica, restauração de tarefas e exclusão permanente.

Este projeto foi desenvolvido como estudo prático de desenvolvimento web backend, persistência de dados e organização de uma aplicação em camadas.

## Funcionalidades

* Criar novas tarefas
* Listar tarefas pendentes
* Visualizar detalhes de uma tarefa
* Editar tarefas pendentes
* Concluir tarefas
* Reabrir tarefas concluídas
* Listar o histórico de tarefas concluídas
* Paginar tarefas concluídas
* Excluir tarefas logicamente
* Listar tarefas excluídas
* Restaurar tarefas excluídas
* Excluir tarefas permanentemente
* Confirmar ações por meio de modais

## Tecnologias utilizadas

### Backend

* Python
* Flask
* SQLite

### Frontend

* HTML5
* CSS3
* JavaScript

## Arquitetura

A aplicação foi organizada em camadas para separar responsabilidades e facilitar a manutenção do código.

## Estrutura do projeto

```text
task-crud-python/
├── app/
│   ├── models/
│   │   ├── __init__.py
│   │   └── taskmodel.py
│   │
│   ├── repositories/
│   │   └── taskrepository.py
│   │
│   ├── routes/
│   │   └── rotas.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── taskservice.py
│   │
│   ├── static/
│   │   ├── css/
│   │   │   ├── concluidas.css
│   │   │   ├── excluidas.css
│   │   │   ├── layout.css
│   │   │   ├── modal.css
│   │   │   ├── style.css
│   │   │   └── task.css
│   │   │
│   │   └── js/
│   │       ├── delete.js
│   │       ├── modal.js
│   │       └── reopen.js
│   │
│   ├── templates/
│   │   ├── components/
│   │   │   ├── deleteconfirmation.html
│   │   │   ├── editmodal.html
│   │   │   ├── reopenconfirmation.html
│   │   │   └── taskinfomodal.html
│   │   │
│   │   ├── base.html
│   │   ├── concluidas.html
│   │   ├── excluidas.html
│   │   └── index.html
│   │
│   ├── __init__.py
│   └── database.py
│
├── instance/
│   └── todo.db
│
├── .gitignore
├── README.MD
├── requirements.txt
└── run.py
```

> O arquivo `instance/todo.db` é criado localmente pela aplicação e não deve ser versionado no Git.

## Pré-requisitos

Para executar o projeto, é necessário ter instalado:

* Python 3
* Git
* `pip`
* suporte à criação de ambientes virtuais com `venv`

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/joaoribeiro-p/task-crud-python.git
```

Entre na pasta do projeto:

```bash
cd task-crud-python
```

### 2. Crie o ambiente virtual

No Linux ou macOS:

```bash
python3 -m venv .venv
```

No Windows:

```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual

No Linux ou macOS:

```bash
source .venv/bin/activate
```

No Windows com PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

No Windows com Prompt de Comando:

```cmd
.venv\Scripts\activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute a aplicação

```bash
python run.py
```

Em algumas distribuições Linux, pode ser necessário usar:

```bash
python3 run.py
```

A aplicação estará disponível normalmente em:

```text
http://127.0.0.1:5000
```

## Banco de dados

A aplicação utiliza SQLite.

O banco é armazenado em:

```text
instance/todo.db
```

Na primeira execução, a aplicação cria automaticamente a pasta `instance` e a tabela necessária, caso ainda não existam.

O banco de dados local está incluído no `.gitignore` para evitar o versionamento de dados pessoais ou registros de desenvolvimento.

## Interface

A página principal é organizada em painéis para:

* criação de tarefas;
* visualização de tarefas pendentes;
* visualização de tarefas concluídas recentemente.

A aplicação também possui páginas separadas para:

* histórico de tarefas concluídas;
* tarefas excluídas.

As ações de visualização, edição, reabertura e exclusão utilizam modais implementados com HTML, CSS e JavaScript.

## Rotas principais

| Método | Rota                     | Função                            |
| ------ | ------------------------ | --------------------------------- |
| `GET`  | `/`                      | Exibe o painel principal          |
| `POST` | `/criar`                 | Cria uma tarefa                   |
| `POST` | `/editar/<task_id>`      | Edita uma tarefa                  |
| `POST` | `/concluir/<task_id>`    | Conclui uma tarefa                |
| `POST` | `/reabrir/<task_id>`     | Reabre uma tarefa concluída       |
| `POST` | `/deletar/<task_id>`     | Realiza a exclusão lógica         |
| `GET`  | `/concluidas`            | Lista tarefas concluídas          |
| `GET`  | `/excluidas`             | Lista tarefas excluídas           |
| `POST` | `/restaurar/<task_id>`   | Restaura uma tarefa excluída      |
| `POST` | `/hard_delete/<task_id>` | Exclui uma tarefa permanentemente |

## Aprendizados

Durante o desenvolvimento deste projeto, foram praticados conceitos como:

* criação de aplicações web com Flask;
* organização de projetos Python;
* separação de responsabilidades em camadas;
* manipulação de banco de dados SQLite;
* criação de operações CRUD;
* validação de regras de negócio;
* utilização de Blueprints;
* renderização de páginas com Jinja2;
* criação de componentes reutilizáveis em templates;
* exclusão lógica e exclusão permanente;
* paginação de registros;
* manipulação do DOM com JavaScript;
* criação e controle de modais;
* uso de Git e GitHub durante a evolução do projeto.

## Limitações conhecidas

Esta versão foi desenvolvida como projeto de estudo e possui algumas limitações:

* não possui sistema de autenticação;
* não possui múltiplos usuários;
* todas as tarefas pertencem a um único contexto;
* não possui proteção CSRF nos formulários;
* não possui testes automatizados;
* não possui API REST;
* não possui busca ou filtros avançados;
* utiliza o servidor de desenvolvimento do Flask;
* não está preparada, sem configurações adicionais, para exposição direta em produção.

## Possíveis evoluções

Algumas funcionalidades que poderiam ser exploradas em projetos futuros:

* autenticação e gerenciamento de usuários;
* organização de tarefas por projetos;
* categorias e etiquetas;
* definição de prioridades;
* datas de vencimento;
* busca e filtros;
* API REST;
* testes automatizados;
* uso de SQLAlchemy;
* migrations de banco de dados;
* deploy com Gunicorn e Nginx;
* containerização com Docker.

Essas funcionalidades não fazem parte do escopo atual da aplicação.

## Status do projeto

Projeto concluído como versão de estudo.

O objetivo desta versão foi praticar o desenvolvimento de uma aplicação CRUD completa, desde a persistência dos dados até a interface web, aplicando separação de responsabilidades e regras de negócio.

Novos conceitos e funcionalidades mais avançadas serão explorados em projetos futuros.

## Autor

Desenvolvido por [João Ribeiro](https://github.com/joaoribeiro-p).
