from flask import Flask, render_template, request, redirect, url_for, flash
from utils import get_tarefas, get_tarefa, criar_tarefa, atualizar_tarefa, deletar_tarefa

app = Flask(__name__)
app.secret_key = "sua_chave_aqui"

@app.route('/')
def home():
    return redirect(url_for('listar'))

@app.route('/tarefas')
def listar():
    lista = get_tarefas()
    return render_template('lista.html', lista=lista)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == "POST":
        data = {
            "nome_tarefa": request.form.get("form_nome"),
            "status": request.form.get("form_status"),
            "data": request.form.get("form_data"),
            "horario": request.form.get("form_horario"),
            "descricao": request.form.get("form_descricao")
        }
        tarefa = criar_tarefa(data)
        if tarefa:
            flash("Tarefa criada com sucesso!", "success")
            return redirect(url_for('listar'))
    return render_template('cadastro.html')

@app.route('/tarefa/<int:id_tarefa>/editar', methods=['GET', 'POST'])
def editar(id_tarefa):
    tarefa = get_tarefa(id_tarefa)
    if not tarefa:
        flash("Tarefa não encontrada.", "error")
        return redirect(url_for('listar'))

    if request.method == "POST":
        data = {
            "nome_tarefa": request.form.get("form_nome"),
            "status": request.form.get("form_status"),
            "data": request.form.get("form_data"),
            "horario": request.form.get("form_horario"),
            "descricao": request.form.get("form_descricao")
        }
        resultado = atualizar_tarefa(id_tarefa, data)
        if resultado:
            flash("Tarefa atualizada com sucesso!", "success")
            return redirect(url_for('listar'))
        else:
            flash("Falha ao atualizar tarefa", "error")

    return render_template('editar.html', tarefa=tarefa)

@app.route('/tarefa/<int:id_tarefa>/delete')
def deletar(id_tarefa):
    if deletar_tarefa(id_tarefa):
        flash("Tarefa deletada com sucesso!", "success")
    else:
        flash("Erro ao deletar tarefa", "error")
    return redirect(url_for('listar'))

if __name__ == '__main__':
    app.run(debug=True)
