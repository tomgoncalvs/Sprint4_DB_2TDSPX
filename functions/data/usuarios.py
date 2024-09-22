from flask import request, redirect, url_for, flash, render_template
from bson.objectid import ObjectId
from functions.config import mongo
from functions.config import bcrypt

# Criar usuário
def create_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']  
        telefone = request.form['telefone']
        data_nascimento = request.form['data_nascimento']

        # Hash da senha
        senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')

        # Inserindo o novo usuário no banco de dados
        novo_usuario = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "senha": senha_hash,
            "data_nascimento": data_nascimento
        }

        mongo.db.USERS.insert_one(novo_usuario)
        flash('Usuário cadastrado com sucesso!', 'success')
        return redirect(url_for('usuarios'))

    return render_template('usuarios/cadastrar.html')


# Listar usuários
def list_usuarios():
    usuarios = mongo.db.USERS.find()
    return render_template('usuarios/list.html', usuarios=usuarios)

# Atualizar usuário
def update_usuario(id):
    usuario = mongo.db.USERS.find_one({"_id": ObjectId(id)})
    if request.method == 'POST':
        atualizacao = {
            "nome": request.form['nome'],
            "email": request.form['email'],
            "data_nascimento": request.form['data_nascimento'],
            "cpf": request.form['cpf'],
            "telefone": request.form['telefone']
        }
        mongo.db.USERS.update_one({"_id": ObjectId(id)}, {"$set": atualizacao})
        flash('Usuário atualizado com sucesso!', 'success')
        return redirect(url_for('list_usuarios'))
    return render_template('usuarios/update.html', usuario=usuario)

# Deletar usuário
def delete_usuario(id):
    try:
        _id = ObjectId(id)
        mongo.db.USERS.delete_one({"_id": _id})
        flash('Usuário deletado com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao deletar o usuário: {str(e)}', 'danger')

    return redirect(url_for('usuarios'))  
