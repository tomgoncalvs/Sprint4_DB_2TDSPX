from flask import redirect, session, flash, url_for

def logout_user():
    session.clear()
    flash('Você saiu da sua conta.', 'info')
    return redirect(url_for('login'))
