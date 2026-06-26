# Prática 4 – Aplicação Monolítica com Django

## Descrição

Este projeto consiste em uma aplicação web desenvolvida utilizando o framework **Django**, com o objetivo de implementar um sistema simples de gerenciamento de tarefas (To-Do List).

A aplicação permite realizar operações de cadastro, visualização, edição e exclusão de tarefas, utilizando o banco de dados **SQLite** para persistência das informações.

Como extensão da atividade proposta em sala de aula, foi desenvolvida uma **API REST** utilizando os recursos nativos do Django, permitindo que as tarefas também possam ser manipuladas através de requisições HTTP e testadas utilizando o **Postman**.

---

# Tecnologias Utilizadas

## Backend

- Python 3.14
- Django 6.0
- SQLite
- ORM do Django

## Frontend

- HTML5
- Bootstrap 5

## Ferramentas

- Git
- GitHub
- Postman

---

# Funcionalidades Implementadas

## Interface Web

A aplicação permite:

- Cadastro de tarefas;
- Listagem das tarefas cadastradas;
- Edição de tarefas;
- Exclusão de tarefas;
- Persistência dos dados em banco SQLite.

---

## API REST

Foi implementada uma API para disponibilizar as informações das tarefas em formato JSON.

A API utiliza os recursos nativos do Django, sem dependências adicionais, permitindo integração entre aplicações e testes através do Postman.

---

# Endpoints da API

| Método | Endpoint                    | Descrição                     |
| ------ | --------------------------- | ----------------------------- |
| GET    | `/api/tarefas/`             | Lista todas as tarefas        |
| GET    | `/api/tarefa/<id>/`         | Retorna uma tarefa específica |
| POST   | `/api/tarefas/nova/`        | Cadastra uma nova tarefa      |
| PUT    | `/api/tarefa/editar/<id>/`  | Atualiza uma tarefa existente |
| DELETE | `/api/tarefa/deletar/<id>/` | Remove uma tarefa             |

---

# Estrutura do Projeto

```text
PRÁTICA 4 - MONOLITICO
│
├── config/
│
├── tarefas/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
├── templates/
│   └── tarefas/
│       ├── lista.html
│       └── form.html
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

# Modelo de Dados

Foi criado o modelo **Tarefa**, contendo os seguintes atributos:

- Nome;
- Descrição;
- Data de início;
- Status.

O status da tarefa possui as seguintes opções:

- Não iniciado;
- Aprovado;
- Paralisado;
- Finalizado.

Os dados são persistidos automaticamente utilizando o ORM do Django.

---

# Arquitetura Utilizada

A aplicação segue a arquitetura **MTV (Model – Template – View)**.

### Model

Responsável pela estrutura dos dados e comunicação com o banco SQLite através do ORM.

### Template

Responsável pela interface gráfica desenvolvida utilizando HTML e Bootstrap.

### View

Responsável pelo processamento das requisições, regras de negócio e comunicação entre Models e Templates.

Além das Views tradicionais, foram implementadas Views específicas para disponibilização da API REST.

---

# Ajustes Realizados Durante o Desenvolvimento

Durante o desenvolvimento da atividade foram realizados diversos ajustes para garantir o correto funcionamento da aplicação.

## Configuração dos Templates

Foi configurado corretamente o arquivo **settings.py**, adicionando a pasta global de templates:

```python
'DIRS': [BASE_DIR / 'templates']
```

Essa configuração permitiu que o Django localizasse corretamente os arquivos HTML da aplicação.

---

## Aplicação das Migrations

Foram executadas as migrations responsáveis pela criação das tabelas do banco SQLite.

```bash
python manage.py migrate
```

---

## Validação do Banco de Dados

Foi realizada a conferência do banco SQLite para verificar:

- criação das tabelas;
- armazenamento correto das tarefas;
- integração entre formulários, Views e banco de dados.

---

## Melhoria da Interface

A interface original foi aprimorada utilizando Bootstrap 5.

Foram adicionados:

- Layout responsivo;
- Cards;
- Botões estilizados;
- Formulários modernos;
- Melhor organização visual;
- Melhor experiência do usuário.

As melhorias foram desenvolvidas considerando princípios de usabilidade e Design Centrado no Usuário.

---

## Implementação da API REST

Além da aplicação web tradicional, foi implementada uma API REST responsável por disponibilizar as informações das tarefas em formato JSON.

As Views da API foram desenvolvidas utilizando **JsonResponse**, permitindo o consumo dos dados por aplicações externas e pelo Postman.

Também foi utilizada a anotação `@csrf_exempt` nas Views da API para permitir testes utilizando clientes externos durante o desenvolvimento da atividade.

---

# Testes Realizados

Todos os endpoints foram testados utilizando o Postman.

Foram realizadas requisições utilizando os seguintes métodos HTTP:

- GET
- POST
- PUT
- DELETE

Os testes confirmaram o correto funcionamento das operações de:

- consulta;
- cadastro;
- atualização;
- remoção de tarefas.

Também foi validada a persistência dos dados no banco SQLite após as operações realizadas pela API.

---

# Como Executar o Projeto

## Criar ambiente virtual

```bash
python -m venv env
```

---

## Ativar ambiente virtual

Windows

```bash
env\Scripts\activate
```

---

## Instalar dependências

```bash
pip install django
```

---

## Executar migrations

```bash
python manage.py migrate
```

---

## Iniciar servidor

```bash
python manage.py runserver
```

---

## Acessar aplicação

```
http://127.0.0.1:8000
```

---

## Testar a API

Exemplos de endpoints disponíveis:

```
GET     /api/tarefas/
GET     /api/tarefa/1/

POST    /api/tarefas/nova/

PUT     /api/tarefa/editar/1/

DELETE  /api/tarefa/deletar/1/
```

Os endpoints podem ser testados utilizando o Postman, enviando e recebendo dados no formato JSON.

---

# Resultado

O projeto demonstra a construção de uma aplicação web monolítica utilizando Django, implementando operações completas de CRUD através da interface web e do banco de dados SQLite.

Como complemento da atividade, foi desenvolvida uma API REST utilizando os recursos nativos do Django, possibilitando o gerenciamento das tarefas através de requisições HTTP e validação utilizando o Postman.

Dessa forma, o projeto reúne conceitos fundamentais de desenvolvimento web, arquitetura MTV, ORM, persistência de dados, APIs REST, integração cliente-servidor e testes de serviços, atendendo aos objetivos propostos pela disciplina.
