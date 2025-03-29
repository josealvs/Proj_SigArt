# **API de Gerenciamento de Tarefas (To-Do List)**

Uma API desenvolvida em **Django** e **Django Rest Framework** para gerenciar uma lista de tarefas (To-Do List). A API permite criar, ler, atualizar, excluir e listar tarefas. Também inclui funcionalidades de busca e validação de dados.

## 🚀 **Tecnologias Usadas**

- **Django**: Framework Python para desenvolvimento web.
- **Django Rest Framework (DRF)**: Biblioteca para criação de APIs RESTful.
- **PostgreSQL**: Banco de dados relacional utilizado para persistência de dados.
- **Docker**: Para containerização da aplicação, facilitando o ambiente de desenvolvimento e produção.

## 📝 **Funcionalidades**

### **Endpoints da API**

1. **Listar todas as tarefas**  
   - **Método:** `GET`  
   - **URL:** `/api/tasks/`  
   - **Descrição:** Retorna uma lista de todas as tarefas. Suporta paginação (5 tarefas por vez).

2. **Buscar tarefas**  
   - **Método:** `GET`  
   - **URL:** `/api/tasks/?search=<termo>`  
   - **Descrição:** Realiza uma busca por título ou descrição das tarefas.

3. **Criar nova tarefa**  
   - **Método:** `POST`  
   - **URL:** `/api/tasks/`  
   - **Descrição:** Cria uma nova tarefa.  
   - **Campos obrigatórios:** `title`, `due_date`, `status`.

4. **Visualizar tarefa específica**  
   - **Método:** `GET`  
   - **URL:** `/api/tasks/<id>/`  
   - **Descrição:** Retorna os detalhes de uma tarefa específica.

5. **Atualizar tarefa existente**  
   - **Método:** `PATCH`  
   - **URL:** `/api/tasks/<id>/`  
   - **Descrição:** Atualiza uma tarefa existente.

6. **Excluir tarefa**  
   - **Método:** `DELETE`  
   - **URL:** `/api/tasks/<id>/`  
   - **Descrição:** Exclui uma tarefa específica.

---

## ⚙️ **Configuração do Projeto**

### **1. Instalar Dependências**

Clone o repositório do projeto e instale as dependências:

```bash
git clone <url-do-repositorio>
cd proj_todo
pip install -r requirements.txt
```

## 2. Configurar o Banco de Dados
Certifique-se de que o PostgreSQL está instalado e configurado. Caso esteja utilizando o Docker, o banco de dados será iniciado automaticamente com o contêiner.

Crie o banco de dados e execute as migrações:

```bash
python manage.py migrate
```

## 3. Criar um Super Usuário(Opcional)
Para acessar o painel de administração do Django, crie um superusuário:

```bash
python manage.py createsuperuser
```

## 🐳 **Rodando a Aplicação com Docker**

### **Endpoints da API**

1. **Construir e Subir os Containers**
   Para rodar a aplicação com Docker, siga os passos abaixo:
   
   - Certifique-se de que o Docker e o Docker Compose estão instalados.

2. Crie um arquivo .env na raiz do projeto com as variáveis de ambiente do banco de dados:

   ```bash
   DATABASE_NAME=mydatabase
   DATABASE_USER=myuser
   DATABASE_PASSWORD=mypassword
   DATABASE_HOST=db
   DATABASE_PORT=5432
   ```
3. **Construa e inicie os containers**  
   ```bash
   docker-compose up --build
   ```
4. **Acesse a aplicação**  
  A aplicação estará disponível em: http://localhost:8000/api/

## 🧪 **Testes**

### **Rodar os Testes Unitários**

 Para rodar os testes unitários e garantir que tudo esteja funcionando corretamente, use:

 ```bash
 python manage.py createsuperuser
 ```
Isso executará os testes definidos no arquivo tasks/tests.py, cobrindo funcionalidades básicas da API, como criação, atualização e exclusão de tarefas.

## 📦 **Estrutura do Projeto**

### **Aqui está a estrutura do seu projeto Django:**

 ```bash
 proj_todo/
│── tasks/                # Aplicação Django para gerenciar as tarefas
│── proj_todo/            # Configurações principais do projeto
│── manage.py             # Comando principal para administrar o Django
│── requirements.txt      # Dependências do projeto
│── Dockerfile            # Configuração do Docker para a aplicação
│── docker-compose.yml    # Orquestração dos containers (Django + PostgreSQL)
│── .env                  # Variáveis de ambiente (banco de dados)
│── .dockerignore         # Ignorar arquivos desnecessários no Docker

 ```
