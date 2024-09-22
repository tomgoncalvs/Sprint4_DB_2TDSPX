from flask import render_template, request, redirect, session, flash, url_for
from functions.config import mongo, bcrypt 

def login_user():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        # Verificar se o usuário existe no banco de dados
        user = mongo.db.USERMASTER.find_one({"email": email})
        if not user:
            flash('Usuário não encontrado.', 'danger')
            return redirect(url_for('login'))

        # Verificar se a senha está correta
        if bcrypt.check_password_hash(user['senha_hash'], senha):
            session['user_id'] = str(user['_id'])
            session['user_role'] = user.get('role', 'user') 
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Senha incorreta.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')
