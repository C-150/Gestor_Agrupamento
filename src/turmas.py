# turmas.py

import json
import os

turmas = {}

FICHEIRO_TURMAS = "turmas.json"

# ==============================
# PERSISTENCIA
# ==============================
def guardar_turmas():
    with open(FICHEIRO_TURMAS, "w", encoding="utf-8") as ficheiro:
        json.dump(turmas, ficheiro, indent=4, ensure_ascii=False)


def carregar_turmas():
    global turmas

    if os.path.exists(FICHEIRO_TURMAS):
        with open(FICHEIRO_TURMAS, "r", encoding="utf-8") as ficheiro:
            turmas = json.load(ficheiro)
    else:
        turmas = {}


# ==============================
# VALIDACOES
# ==============================
def validar_texto(txt):
    return isinstance(txt, str) and len(txt.strip()) > 0


# ==============================
# CREATE
# ==============================
def criar_turma(id_turma, descricao, id_curso):
    carregar_turmas()

    if not validar_texto(id_turma):
        return 400, "ID invalido"

    if not validar_texto(descricao):
        return 400, "Descricao invalida"

    if id_turma in turmas:
        return 409, "Turma ja existe"

    turmas[id_turma] = {
        "id_turma": id_turma,
        "descricao": descricao,
        "horarios": [],
        "alunos": {},
        "id_curso": id_curso
    }

    guardar_turmas()
    return 201, turmas[id_turma]


# ==============================
# READ
# ==============================
def listar_turmas():
    carregar_turmas()

    if not turmas:
        return 404, "Nenhuma turma encontrada"

    lista = []

    for t in turmas.values():
        lista.append(
            f"ID: {t['id_turma']} | Nome: {t['descricao']} | Alunos: {len(t['alunos'])}"
        )

    return 200, lista


# ==============================
# SEARCH
# ==============================
def pesquisar_turma(texto):
    carregar_turmas()

    resultados = {}

    for id_t, t in turmas.items():
        if texto.lower() in t["descricao"].lower():
            resultados[id_t] = t

    if not resultados:
        return 404, "Nenhuma turma encontrada"

    return 200, resultados


# ==============================
# STATS
# ==============================
def estatisticas_turmas():
    carregar_turmas()

    if not turmas:
        return 404, "Sem turmas registadas"

    total_turmas = len(turmas)
    total_alunos = sum(len(t["alunos"]) for t in turmas.values())

    return 200, {
        "total_turmas": total_turmas,
        "total_alunos": total_alunos
    }


# ==============================
# UPDATE
# ==============================
def atualizar_turma(id_turma, nova_descricao):
    carregar_turmas()

    if id_turma not in turmas:
        return 404, "Turma nao encontrada"

    if not validar_texto(nova_descricao):
        return 400, "Descricao invalida"

    turmas[id_turma]["descricao"] = nova_descricao

    guardar_turmas()
    return 200, turmas[id_turma]


# ==============================
# DELETE
# ==============================
def apagar_turma(id_turma):
    carregar_turmas()

    if id_turma not in turmas:
        return 404, "Turma nao encontrada"

    del turmas[id_turma]

    guardar_turmas()
    return 200, id_turma
