from flask import Flask, jsonify, request
from models import Tarefa, db_session, init_db

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# Listar todas as tarefas
@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    tarefas = db_session.query(Tarefa).all()
    return jsonify([t.serialize_tarefa() for t in tarefas])

# Buscar tarefa por ID
@app.route('/tarefas/<int:id_tarefa>', methods=['GET'])
def buscar_tarefa(id_tarefa):
    tarefa = db_session.query(Tarefa).get(id_tarefa)
    if tarefa:
        return jsonify(tarefa.serialize_tarefa())
    return jsonify({"error": "Tarefa não encontrada"}), 404

# Criar nova tarefa
@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.get_json()
    campos_necessarios = ["nome_tarefa", "status", "data", "horario", "descricao"]
    if not all(campo in dados for campo in campos_necessarios):
        return jsonify({"error": "Campos obrigatórios ausentes"}), 400

    nova_tarefa = Tarefa(**dados)
    nova_tarefa.save()
    return jsonify(nova_tarefa.serialize_tarefa()), 201

# Atualizar tarefa existente
@app.route('/tarefas/<int:id_tarefa>', methods=['PUT'])
def atualizar_tarefa(id_tarefa):
    tarefa = db_session.query(Tarefa).get(id_tarefa)
    if not tarefa:
        return jsonify({"error": "Tarefa não encontrada"}), 404

    dados = request.get_json()
    for campo in ["nome_tarefa", "status", "data", "horario", "descricao"]:
        if campo in dados:
            setattr(tarefa, campo, dados[campo])
    db_session.commit()
    return jsonify(tarefa.serialize_tarefa())

# Deletar tarefa
@app.route('/tarefas/<int:id_tarefa>', methods=['DELETE'])
def deletar_tarefa(id_tarefa):
    tarefa = db_session.query(Tarefa).get(id_tarefa)
    if not tarefa:
        return jsonify({"error": "Tarefa não encontrada"}), 404

    tarefa.delete()
    return jsonify({"message": "Tarefa deletada com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)