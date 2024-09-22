# Gestão de Banco de Dados em Flask e MongoDB

Este projeto foi desenvolvido para a disciplina MASTERING RELATIONAL AND NON-RELATIONAL DATABASE - Professor: Renê de Ávila Mendes. Criamos uma aplicação web utilizando Flask com integração ao banco de dados MongoDB. A aplicação permite realizar o CRUD (Create, Read, Update, Delete) em várias coleções, como usuários, compras, categorias, campanhas e produtos. Além disso, há uma funcionalidade de exportação de dados do banco para um arquivo CSV.

# Integrantes do Grupo
- Beatriz Lucas - RM99104
- Enzo Farias - RM 98792
- Ewerton Gonçalves - RM98571
- Guilherme Tantulli - RM97890
- Thiago Zupelli - RM99085

## Funcionalidades

### 1. **CRUD de Usuários**
- Listar todos os usuários.
- Adicionar um novo usuário.
- Editar um usuário existente.
- Excluir um usuário.

### 2. **CRUD de Compras**
- Listar todas as compras realizadas.
- Adicionar uma nova compra, escolhendo o usuário e o produto.
- Editar os detalhes de uma compra.
- Excluir uma compra.

### 3. **CRUD de Categorias**
- Listar todas as categorias cadastradas.
- Adicionar uma nova categoria.
- Editar uma categoria existente.
- Excluir uma categoria.

### 4. **CRUD de Produtos**
- Listar todos os produtos cadastrados.
- Adicionar um novo produto.
- Editar um produto existente.
- Excluir um produto.

### 5. **Exportação de Dados**
- Exporta os dados de usuários, campanhas e produtos em um arquivo CSV.

## Estrutura do Projeto

- **app.py**: Arquivo principal que contém as rotas e a lógica principal da aplicação.
- **functions**: Contém as funções modulares que gerenciam diferentes aspectos da aplicação, como login, registro, dashboard, manipulação de dados de compras, categorias e usuários.
- **templates**: Contém os arquivos HTML, organizados para renderizar os dados dinamicamente no frontend.
- **static**: Contém os arquivos estáticos como CSS e JavaScript (se necessário).

## Dependências e Extensões Utilizadas

### 1. **Flask**
- Framework web utilizado para criar a aplicação e manipular as rotas.

### 2. **Flask-PyMongo**
- Extensão utilizada para integrar o Flask com o banco de dados MongoDB.

### 3. **bcrypt**
- Biblioteca utilizada para realizar o hash das senhas de usuários no registro.

### 4. **dotenv**
- Utilizado para carregar variáveis de ambiente, como a URI do MongoDB e a chave secreta do Flask.

### 5. **csv** e **json**
- Bibliotecas padrão do Python utilizadas para manipulação de arquivos CSV e JSON.

### 6. **io**
- Utilizado para criar um arquivo em memória para a exportação dos dados.

### 7. **bson**
- Extensão necessária para manipular objetos como `ObjectId` do MongoDB.

## Pré-requisitos

1. **Python 3.9 ou superior**.
2. **MongoDB**: Certifique-se de ter um banco de dados MongoDB configurado, seja local ou hospedado na nuvem (como o MongoDB Atlas).
3. **pip**: Instalador de pacotes do Python para gerenciar as dependências.

## Como Instalar e Rodar o Projeto

1. Clone o repositório:

   ```bash
   git clone https://github.com/usuario/projeto-flask-mongo.git
   cd projeto-flask-mongo

2. Crie um ambiente virtual:
- python3 -m venv venv
- source venv/bin/activate  # No Windows use: venv\Scripts\activate

3. Instale as dependências:
- pip install -r requirements.txt

4. Crie um arquivo .env na raiz do projeto com as seguintes variáveis de ambiente:
- SECRET_KEY='sua-chave-secreta-aqui'
- MONGO_URI='mongodb://seu-usuario:senha@localhost:27017/seu-banco'

5. Inicie a Aplicação:
- flask run
6. **A aplicação estará disponível no endereço http://127.0.0.1:5000**

## Estrutura das Rotas

### Usuários
- **`/usuarios`**: Lista os usuários cadastrados.
- **`/usuarios/create`**: Formulário para criar um novo usuário.
- **`/usuarios/update/<id>`**: Formulário para atualizar um usuário existente.
- **`/usuarios/delete/<id>`**: Exclui um usuário.

### Compras
- **`/compras`**: Lista todas as compras.
- **`/compras/cadastrar`**: Formulário para cadastrar uma nova compra.
- **`/compras/editar/<id>`**: Formulário para editar uma compra existente.
- **`/compras/deletar/<id>`**: Exclui uma compra.

### Categorias
- **`/categorias`**: Lista todas as categorias.
- **`/categorias/create`**: Formulário para criar uma nova categoria.
- **`/categorias/update/<id>`**: Formulário para atualizar uma categoria existente.
- **`/categorias/delete/<id>`**: Exclui uma categoria.

### Produtos
- **`/produtos`**: Lista todos os produtos cadastrados.
- **`/produtos/create`**: Formulário para criar um novo produto.
- **`/produtos/update/<id>`**: Formulário para atualizar um produto existente.
- **`/produtos/delete/<id>`**: Exclui um produto.

### Exportação
- **`/export_db`**: Exporta os dados de usuários, campanhas e produtos em um arquivo CSV.

## Considerações Finais

Este projeto foi desenvolvido para ser uma solução completa de gerenciamento de banco de dados MongoDB em um ambiente web utilizando Flask. Todas as operações de CRUD foram implementadas com interface amigável e validação de dados. A funcionalidade de exportação de dados permite facilmente extrair informações do banco em formato CSV, facilitando o uso e análise externa.
