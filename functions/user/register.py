from flask import request, flash, redirect, url_for, render_template
from functions.config import mongo, bcrypt

def register_user():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        nome = request.form['nome']
        
        # Verifica se o email já está cadastrado
        user = mongo.db.USERMASTER.find_one({"email": email})
        if user:
            flash('Usuário já cadastrado', 'danger')
            return redirect(url_for('register'))
        
        # Cria o novo usuário
        senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')
        novo_usuario = {
            "nome_usuario": nome,
            "email": email,
            "senha_hash": senha_hash,
            "role": "admin"
        }
        mongo.db.USERMASTER.insert_one(novo_usuario)
        flash('Cadastro realizado com sucesso', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')
