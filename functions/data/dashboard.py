from flask import render_template, session, redirect, url_for
from functions.config import mongo

def get_dashboard_data():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # Contagem de documentos em cada coleção
    total_usuarios = mongo.db.USERS.count_documents({})
    total_campanhas = mongo.db.CAMPANHAS.count_documents({})
    total_produtos = mongo.db.PRODUTOS.count_documents({})
    total_compras = mongo.db.COMPRAS.count_documents({})
    total_creditos = mongo.db.CREDIT.count_documents({})
    total_notificacoes = mongo.db.NOTIFICACOES.count_documents({})

    return render_template(
        'dashboard.html',
        total_usuarios=total_usuarios,
        total_campanhas=total_campanhas,
        total_produtos=total_produtos,
        total_compras=total_compras,
        total_creditos=total_creditos,
        total_notificacoes=total_notificacoes
    )
