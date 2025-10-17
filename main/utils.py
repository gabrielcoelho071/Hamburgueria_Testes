import requests
from flask import flash

BASE_URL = "http://10.135.235.26:5000/tarefas"  # URL da sua API

def get_tarefas():
    try:
        r = requests.get(BASE_URL)
        r.raise_for_status()
        return r.json()
    except requests.RequestException as e:
        flash(f"Erro ao buscar tarefas: {e}", "error")
        return []

def get_tarefa(id_tarefa):
    try:
        r = requests.get(f"{BASE_URL}/{id_tarefa}")
        r.raise_for_status()
        return r.json()
    except requests.RequestException as e:
        flash(f"Erro ao buscar a tarefa: {e}", "error")
        return None

def criar_tarefa(data):
    try:
        r = requests.post(BASE_URL, json=data)
        r.raise_for_status()
        return r.json()
    except requests.RequestException as e:
        flash(f"Erro ao criar tarefa: {e}", "error")
        return None

def atualizar_tarefa(id_tarefa, data):
    try:
        r = requests.put(f"{BASE_URL}/{id_tarefa}", json=data)
        r.raise_for_status()
        return r.json()
    except requests.RequestException as e:
        flash(f"Erro ao atualizar tarefa: {e}", "error")
        return None

def deletar_tarefa(id_tarefa):
    try:
        r = requests.delete(f"{BASE_URL}/{id_tarefa}")
        r.raise_for_status()
        return True
    except requests.RequestException as e:
        flash(f"Erro ao deletar tarefa: {e}", "error")
        return False
