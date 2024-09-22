from flask import request, redirect, url_for, flash, render_template
from bson.objectid import ObjectId
from functions.config import mongo

# Criar categoria
def create_categoria():
    if request.method == 'POST':
        nova_categoria = {
            "nome_categoria": request.form['nome_categoria'],
            "descricao": request.form['descricao']
        }
        mongo.db.CATEGORIAS.insert_one(nova_categoria)
        flash('Categoria cadastrada com sucesso!', 'success')
        return redirect(url_for('categorias'))
    return render_template('categorias/create.html')

# Listar categorias
def list_categorias():
    categorias = mongo.db.CATEGORIAS.find()
    return render_template('categorias/list.html', categorias=categorias)

# Atualizar categoria
def update_categoria(id):
    try:
        _id = ObjectId(id) 
        novo_nome = request.form['nome_categoria']
        nova_descricao = request.form['descricao']

        # Atualiza a categoria no banco de dados
        mongo.db.CATEGORIAS.update_one(
            {"_id": _id},
            {"$set": {"nome_categoria": novo_nome, "descricao": nova_descricao}}
        )

        flash('Categoria atualizada com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao atualizar a categoria: {str(e)}', 'danger')

    return redirect(url_for('categorias'))  


# Deletar categoria
def delete_categoria(id):
    try:
        _id = ObjectId(id) 
        mongo.db.CATEGORIAS.delete_one({"_id": _id})
        flash('Categoria deletada com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao deletar a categoria: {str(e)}', 'danger')

    
    return redirect(url_for('categorias'))  

