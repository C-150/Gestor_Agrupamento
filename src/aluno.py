# aluno.py

import json
import os

from utils import validar_email, validar_nome, validar_numero

alunos = {}

FICHEIRO_ALUNOS = "alunos.json"


# ==============================
# PERSISTENCIA
# ==============================
def guardar_alunos():
    with open(FICHEIRO_ALUNOS, "w", encoding="utf-8") as ficheiro:
        json.dump(alunos, ficheiro, indent=4, ensure_ascii=False)


def carregar_alunos():
    global alunos

    if os.path.exists(FICHEIRO_ALUNOS):
        with open(FICHEIRO_ALUNOS, "r", encoding="utf-8") as ficheiro:
            alunos = json.load(ficheiro)
    else:
        alunos = {}


# ==============================
# CREATE
# ==============================
def criar_aluno(numero, nome, email, telefone, data_nascimento, id_turma):
    carregar_alunos()

    if not validar_numero(numero):
        return 400, "Numero de aluno invalido"

    if not validar_nome(nome):
        return 400, "Nome invalido"

    if not validar_email(email):
        return 400, "Email invalido"

    if numero in alunos:
        return 409, "Aluno ja existe"

    aluno = {
        "numero_aluno": numero,
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "data_nascimento": data_nascimento,
        "id_turma": id_turma
    }

    alunos[numero] = aluno
    guardar_alunos()

    return 201, aluno


# ==============================
# READ
# ==============================
def listar_alunos():
    carregar_alunos()

    if not alunos:
        return 404, "Nenhum aluno encontrado"

    lista = []

    for aluno in alunos.values():
        lista.append(
            f"Nº: {aluno['numero_aluno']} | Nome: {aluno['nome']} | Turma: {aluno['id_turma']}"
        )

    return 200, lista


# ==============================
# SEARCH
# ==============================
def pesquisar_aluno(texto):
    carregar_alunos()

    resultados = {}

    for num, aluno in alunos.items():
        if texto.lower() in aluno["nome"].lower() or texto in aluno["email"]:
            resultados[num] = aluno

    if not resultados:
        return 404, "Nenhum aluno encontrado"

    return 200, resultados


# ==============================
# STATS
# ==============================
def estatisticas_alunos():
    carregar_alunos()

    total = len(alunos)

    if total == 0:
        return 404, "Sem alunos registados"

    return 200, {
        "total_alunos": total
    }


# ==============================
# UPDATE
# ==============================
def atualizar_aluno(numero, novo_nome=None, novo_email=None):
    carregar_alunos()

    if numero not in alunos:
        return 404, "Aluno nao encontrado"

    if novo_nome is not None:
        if not validar_nome(novo_nome):
            return 400, "Nome invalido"
        alunos[numero]["nome"] = novo_nome

    if novo_email is not None:
        if not validar_email(novo_email):
            return 400, "Email invalido"
        alunos[numero]["email"] = novo_email

    guardar_alunos()
    return 200, alunos[numero]


# ==============================
# DELETE
# ==============================
def apagar_aluno(numero):
    carregar_alunos()

    if numero not in alunos:
        return 404, "Aluno nao encontrado"

    aluno_eliminado = alunos[numero]
    del alunos[numero]
    guardar_alunos()

    return 200, aluno_eliminado
