from flask import Flask, request, render_template, redirect, session, flash, url_for, send_file
from dotenv import load_dotenv
from functions.config import mongo, bcrypt
from functions.user.login import login_user
from functions.user.register import register_user
from functions.user.logout import logout_user
from functions.data.dashboard import get_dashboard_data
from functions.data.compras import create_compra, listar_compras, update_compra, delete_compra
from functions.data.categorias import create_categoria, list_categorias, update_categoria, delete_categoria
from functions.data.usuarios import create_usuario, list_usuarios, update_usuario, delete_usuario
from bson import ObjectId, errors
import os
import io
import csv
import json
from datetime import datetime

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Configuração do MongoDB
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo.init_app(app)
bcrypt.init_app(app)

# Função para serializar datetime e ObjectId
def json_serial(obj):
    """Função para serializar objetos que não podem ser serializados por padrão pelo json.dumps."""
    if isinstance(obj, (datetime, ObjectId)):
        return str(obj)
    raise TypeError(f"Tipo {type(obj)} não é serializável para JSON")

# Rotas de login, registro e logout
@app.route('/login', methods=['GET', 'POST'])
def login():
    return login_user()

@app.route('/register', methods=['GET', 'POST'])
def register():
    return register_user()

@app.route('/logout')
def logout():
    return logout_user()

# Rota para o dashboard
@app.route('/dashboard')
def dashboard():
    return get_dashboard_data()

# CRUD de compras
@app.route('/compras', methods=['GET', 'POST'])
def compras():
    if request.method == 'POST':
        return create_compra()
    return listar_compras()

@app.route('/compras/cadastrar', methods=['GET', 'POST'])
def cadastrar_compra():
    if request.method == 'POST':
        id_usuario = request.form['id_usuario']
        id_produto = request.form['id_produto']
        quantidade = request.form['quantidade']
        valor_total = request.form['valor_total']

        nova_compra = {
            "id_usuario": id_usuario,
            "id_produto": id_produto,
            "quantidade": quantidade,
            "valor_total": valor_total,
            "data_compra": datetime.now()
        }

        mongo.db.COMPRAS.insert_one(nova_compra)
        flash('Compra cadastrada com sucesso!', 'success')
        return redirect(url_for('compras'))

    # Buscar usuários e produtos para exibir no select
    usuarios = mongo.db.USERS.find()
    produtos = mongo.db.PRODUTOS.find()

    return render_template('compras/cadastrar.html', usuarios=usuarios, produtos=produtos)


@app.route('/compras/editar/<id>', methods=['POST'])
def editar_compra(id):
    return update_compra(id)

@app.route('/compras/deletar/<id>', methods=['POST'])
def deletar_compra(id):
    return delete_compra(id)

# CRUD de categorias
@app.route('/categorias/create', methods=['GET', 'POST'])
def create_categorias():
    return create_categoria()

@app.route('/categorias', methods=['GET'])
def categorias():
    return list_categorias()

@app.route('/categorias/update/<id>', methods=['GET', 'POST'])
def update_categorias(id):
    return update_categoria(id)

@app.route('/categorias/delete/<id>')
def delete_categorias(id):
    return delete_categoria(id)

# CRUD de usuários
@app.route('/usuarios/create', methods=['GET', 'POST'])
def create_usuarios():
    return create_usuario()

@app.route('/usuarios', methods=['GET'])
def usuarios():
    return list_usuarios()

@app.route('/usuarios/update/<id>', methods=['GET', 'POST'])
def update_usuarios(id):
    return update_usuario(id)

@app.route('/usuarios/delete/<id>')
def delete_usuarios(id):
    return delete_usuario(id)

# Página inicial que redireciona para login
@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

# Função para exportar o banco de dados
@app.route('/export_db', methods=['GET'])
def export_db():
    # Exportar usuários
    usuarios = mongo.db.USERS.find()
    campanhas = mongo.db.CAMPANHAS.find()
    produtos = mongo.db.PRODUTOS.find()

    # Criar um arquivo CSV ou JSON para exportar
    output = io.StringIO()
    writer = csv.writer(output)

    # Escrever o cabeçalho do CSV
    writer.writerow(['Coleção', 'Dados'])

    # Exportar dados de cada coleção como JSON em uma linha, usando a função de serialização
    for usuario in usuarios:
        writer.writerow(['USERS', json.dumps(usuario, default=json_serial)])
    for campanha in campanhas:
        writer.writerow(['CAMPANHAS', json.dumps(campanha, default=json_serial)])
    for produto in produtos:
        writer.writerow(['PRODUTOS', json.dumps(produto, default=json_serial)])

    # Ajustar o ponteiro do arquivo
    output.seek(0)

    # Enviar o arquivo CSV como resposta
    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype='text/csv',
        as_attachment=True,
        download_name='export_banco_dados.csv'
    )

if __name__ == '__main__':
    app.run(debug=True)
