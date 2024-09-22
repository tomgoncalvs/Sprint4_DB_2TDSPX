from flask import render_template, request, redirect, flash, url_for
from bson import ObjectId
from datetime import datetime
from functions.config import mongo

# Função para listar compras
# Função para listar compras
def listar_compras():
    compras = mongo.db.COMPRAS.find()
    compras_detalhadas = []

    for compra in compras:
        id_usuario = compra['id_usuario']
        id_produto = compra['id_produto']

        # Tentativa de buscar por ObjectId
        usuario = None
        produto = None

        # Tentar como ObjectId primeiro
        try:
            if isinstance(id_usuario, str):
                id_usuario = ObjectId(id_usuario)
            if isinstance(id_produto, str):
                id_produto = ObjectId(id_produto)

            usuario = mongo.db.USERS.find_one({"_id": id_usuario})
            produto = mongo.db.PRODUTOS.find_one({"_id": id_produto})
        except:
            pass

        # Se não encontrar com ObjectId, tentar como int
        if not usuario:
            usuario = mongo.db.USERS.find_one({"_id": int(id_usuario)})
        if not produto:
            produto = mongo.db.PRODUTOS.find_one({"_id": int(id_produto)})

        compra_detalhada = {
            "_id": compra["_id"],
            "usuario": usuario['nome'] if usuario else "Usuário não encontrado",
            "produto": produto['nome_produto'] if produto else "Produto não encontrado",
            "quantidade": compra['quantidade'],
            "valor_total": compra['valor_total']
        }

        compras_detalhadas.append(compra_detalhada)

    # Obter todos os usuários e produtos para o modal de cadastro
    usuarios = mongo.db.USERS.find()
    produtos = mongo.db.PRODUTOS.find()

    return render_template('compras/list.html', compras=compras_detalhadas, usuarios=usuarios, produtos=produtos)




# Função para criar nova compra
def create_compra():
    if request.method == 'POST':
        id_usuario = request.form['id_usuario']
        id_produto = request.form['id_produto']
        quantidade = int(request.form['quantidade'])
        valor_total = float(request.form['valor_total'])

        # Tentativa de converter os IDs para ObjectId
        try:
            id_usuario = ObjectId(id_usuario)
        except:
            # Se falhar, trate como um int (provavelmente o ID é um int)
            id_usuario = int(id_usuario)
        
        try:
            id_produto = ObjectId(id_produto)
        except:
            # Se falhar, trate como um int (provavelmente o ID é um int)
            id_produto = int(id_produto)

        nova_compra = {
            "id_usuario": id_usuario,
            "id_produto": id_produto,
            "quantidade": quantidade,
            "data_compra": datetime.now(),
            "valor_total": valor_total
        }

        mongo.db.COMPRAS.insert_one(nova_compra)
        flash('Compra cadastrada com sucesso!', 'success')
        return redirect(url_for('compras'))

    # Buscar usuários e produtos para exibir no select
    usuarios = mongo.db.USERS.find()
    produtos = mongo.db.PRODUTOS.find()

    return render_template('compras/cadastrar.html', usuarios=usuarios, produtos=produtos)


# Função para atualizar uma compra
def update_compra(id):
    try:
        _id = ObjectId(id)
        nova_quantidade = int(request.form['quantidade'])
        novo_valor_total = float(request.form['valor_total'])

        mongo.db.COMPRAS.update_one(
            {"_id": _id},
            {"$set": {"quantidade": nova_quantidade, "valor_total": novo_valor_total}}
        )

        flash('Compra atualizada com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao atualizar a compra: {str(e)}', 'danger')

    return redirect(url_for('compras'))

# Função para deletar uma compra
def delete_compra(id):
    try:
        _id = ObjectId(id)
        mongo.db.COMPRAS.delete_one({"_id": _id})
        flash('Compra deletada com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao deletar a compra: {str(e)}', 'danger')

    return redirect(url_for('compras'))
