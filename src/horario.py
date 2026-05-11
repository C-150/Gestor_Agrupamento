# horario.py
import json
import os
from turmas import turmas
from curso import validar_id, validar_nome, validar_duracao
from utils import validar_id , validar_lista
horarios = {}


FICHEIRO_HORARIOS = "horarios.json"


# ==============================
# PERSISTENCIA
# ==============================
def guardar_horarios():
    with open(FICHEIRO_HORARIOS, "w", encoding="utf-8") as ficheiro:
        json.dump(horarios, ficheiro, indent=4, ensure_ascii=False)


def carregar_horarios():
    global horarios

    if os.path.exists(FICHEIRO_HORARIOS):
        with open(FICHEIRO_HORARIOS, "r", encoding="utf-8") as ficheiro:
            horarios = json.load(ficheiro)
    else:
        horarios = {}

# ==============================
# CREATE
# ==============================
def criar_horario(id_horario, id_turma, lista_disciplina, lista_professor):

    if not validar_id(id_horario):
        return 400, "ID invalido"

    if id_horario in horarios:
        return 409, "Horario ja existe"

    if id_turma not in turmas:
        return 404, "Turma nao existe"

    if not validar_lista(lista_disciplina):
        return 400, "Lista de disciplinas invalida"

    if not validar_lista(lista_professor):
        return 400, "Lista de professores invalida"

    # ==============================
    # ATRIBUTOS DO HORARIO
    # ==============================
    horario = {
        "id_horario": id_horario,
        "id_turma": id_turma,
        "lista_disciplina": lista_disciplina,
        "lista_professor": lista_professor
    }

    horarios[id_horario] = horario

    return 201, horario


# ==============================
# READ
# ==============================
def listar_horarios():

    if not horarios:
        return 404, "Nenhum horario encontrado"

    lista = []

    for h in horarios.values():
        lista.append(
            f"ID: {h['id_horario']} | Turma: {h['id_turma']} | Disciplinas: {h['lista_disciplina']}"
        )

    return 200, lista


# ==============================
# UPDATE
# ==============================
def atualizar_horario(id_horario, novas_disciplinas=None, novos_professores=None):

    if id_horario not in horarios:
        return 404, "Horario nao encontrado"

    if novas_disciplinas is not None:
        if not validar_lista(novas_disciplinas):
            return 400, "Lista invalida"
        horarios[id_horario]["lista_disciplina"] = novas_disciplinas

    if novos_professores is not None:
        if not validar_lista(novos_professores):
            return 400, "Lista invalida"
        horarios[id_horario]["lista_professor"] = novos_professores

    return 200, horarios[id_horario]


# ==============================
# DELETE
# ==============================
def apagar_horario(id_horario):

    if id_horario not in horarios:
        return 404, "Horario nao encontrado"

    removido = horarios[id_horario]
    del horarios[id_horario]

    return 200, removido
