# turmas.py

turmas = {}


# ==============================
# VALIDACOES
# ==============================
def _validar_texto(txt):
    return isinstance(txt, str) and len(txt.strip()) > 0


# ==============================
# CREATE
# ==============================
def criar_turma(id_turma, descricao):

    if not _validar_texto(id_turma):
        return 400, "ID invalido"

    if not _validar_texto(descricao):
        return 400, "Descricao invalida"

    if id_turma in turmas:
        return 409, "Turma ja existe"

    turmas[id_turma] = {
        "id_turma": id_turma,
        "descricao": descricao,
        "horarios": [],
        "alunos": {}
    }

    return 201, f"Turma {id_turma} criada com sucesso"


# ==============================
# READ
# ==============================
def listar_turmas():

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

    if id_turma not in turmas:
        return 404, "Turma nao encontrada"

    if not _validar_texto(nova_descricao):
        return 400, "Descricao invalida"

    turmas[id_turma]["descricao"] = nova_descricao

    return 200, "Turma atualizada com sucesso"


# ==============================
# DELETE
# ==============================
def apagar_turma(id_turma):

    if id_turma not in turmas:
        return 404, "Turma nao encontrada"

    del turmas[id_turma]

    return 200, "Turma removida com sucesso"
