# curso.py

import json
import os

from utils import validar_id, validar_nome, validar_duracao

cursos = {}

FICHEIRO_CURSOS = "cursos.json"


# ==============================
# PERSISTENCIA
# ==============================
def guardar_cursos():
    with open(FICHEIRO_CURSOS, "w", encoding="utf-8") as ficheiro:
        json.dump(cursos, ficheiro, indent=4, ensure_ascii=False)


def carregar_cursos():
    global cursos

    if os.path.exists(FICHEIRO_CURSOS):
        with open(FICHEIRO_CURSOS, "r", encoding="utf-8") as ficheiro:
            cursos = json.load(ficheiro)
    else:
        cursos = {}


# ==============================
# CREATE
# ==============================
def criar_curso(id_curso, nome, descricao, duracao):
    carregar_cursos()

    if not validar_id(id_curso):
        return 400, "ID do curso invalido"

    if not validar_nome(nome):
        return 400, "Nome invalido"

    if not validar_duracao(duracao):
        return 400, "Duracao invalida"

    if id_curso in cursos:
        return 409, "Curso ja existe"

    curso = {
        "id_curso": id_curso,
        "nome": nome,
        "descricao": descricao,
        "duracao": duracao
    }

    cursos[id_curso] = curso

    guardar_cursos()
    return 201, curso


# ==============================
# READ
# ==============================
def listar_cursos():
    carregar_cursos()

    if not cursos:
        return 404, "Nenhum curso encontrado"

    lista = []

    for curso in cursos.values():
        lista.append(
            f"ID: {curso['id_curso']} | Nome: {curso['nome']} | Duracao: {curso['duracao']}"
        )

    return 200, lista


# ==============================
# UPDATE
# ==============================
def atualizar_curso(id_curso, novo_nome=None, nova_duracao=None):
    carregar_cursos()

    if id_curso not in cursos:
        return 404, "Curso nao encontrado"

    if novo_nome is not None:
        if not validar_nome(novo_nome):
            return 400, "Nome invalido"
        cursos[id_curso]["nome"] = novo_nome

    if nova_duracao is not None:
        if not validar_duracao(nova_duracao):
            return 400, "Duracao invalida"
        cursos[id_curso]["duracao"] = nova_duracao

    guardar_cursos()
    return 200, cursos[id_curso]


# ==============================
# DELETE
# ==============================
def apagar_curso(id_curso):
    carregar_cursos()

    if id_curso not in cursos:
        return 404, "Curso nao encontrado"

    removido = cursos[id_curso]
    del cursos[id_curso]

    guardar_cursos()
    return 200, removido
