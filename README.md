# Prática 4 – Aplicação Monolítica com Django

## Descrição

Este projeto consiste em uma aplicação web desenvolvida utilizando o framework Django, com o objetivo de implementar um sistema simples de gerenciamento de tarefas (To-Do List).

A aplicação permite realizar operações de cadastro, visualização, edição e exclusão de tarefas, utilizando banco de dados SQLite para persistência dos dados.

---

## Tecnologias Utilizadas

- Python 3.14
- Django 6.0
- SQLite
- HTML
- Bootstrap 5
- Git e GitHub

---

## Funcionalidades Implementadas

### Cadastro de tarefas

O usuário pode cadastrar novas tarefas informando:

- Nome
- Descrição
- Data de início
- Status

### Listagem de tarefas

Todas as tarefas cadastradas são exibidas na página principal.

### Edição de tarefas

Permite alterar informações de tarefas já cadastradas.

### Exclusão de tarefas

Permite remover tarefas do sistema.

### Persistência de dados

As informações são armazenadas no banco de dados SQLite através do ORM do Django.

---

## Estrutura do Projeto

PRÁTICA 4 - MONOLITICO
│
├── config/
├── tarefas/
├── templates/
│ └── tarefas/
│ ├── lista.html
│ └── form.html
├── db.sqlite3
├── manage.py
└── README.md

---

## Ajustes Realizados Durante o Desenvolvimento

Além da implementação proposta em sala de aula, foram realizados os seguintes ajustes:

### Correção da configuração de templates

Foi necessário configurar corretamente o arquivo `settings.py`, adicionando a pasta global de templates:

'DIRS': [BASE_DIR / 'templates']

Essa alteração permitiu que o Django localizasse os arquivos:

- lista.html
- form.html

---

### Aplicação das migrations

Foram executadas as migrations do Django para criação das tabelas necessárias no banco de dados:

python manage.py migrate

---

### Verificação do banco de dados

Foi realizada a validação dos dados diretamente no banco SQLite, confirmando:

- criação de registros;
- armazenamento correto das tarefas;
- integração entre formulário, views e banco de dados.

---

### Melhoria da Interface

A interface original foi aprimorada utilizando Bootstrap 5.

Foram adicionados:

- Layout responsivo;
- Cards para organização das tarefas;
- Botões estilizados;
- Formulários modernos;
- Melhor organização visual das informações;
- Melhor experiência do usuário.

Essas melhorias foram implementadas com foco em usabilidade e design centrado no usuário, temas abordados na disciplina.

---

## Como Executar o Projeto

### 1. Criar ambiente virtual

python -m venv env

### 2. Ativar ambiente virtual

Windows:

env\Scripts\activate

### 3. Instalar Django

pip install django

### 4. Executar migrations

python manage.py migrate

### 5. Iniciar servidor

python manage.py runserver

### 6. Acessar aplicação

http://127.0.0.1:8000

---

## Resultado

O sistema permite gerenciar tarefas através de uma aplicação web desenvolvida em Django, utilizando banco de dados SQLite e interface responsiva construída com Bootstrap, demonstrando os conceitos de desenvolvimento web monolítico estudados na disciplina.
