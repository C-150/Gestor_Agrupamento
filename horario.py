# horario.py

from turmas import turmas

horarios = {}


# ==============================
# VALIDACOES
# ==============================
def _validar_id(id_horario):
    return isinstance(id_horario, str) and len(id_horario.strip()) > 0


def _validar_lista(lista):
    return isinstance(lista, list)


# ==============================
# CREATE
# ==============================
def criar_horario(id_horario, id_turma, lista_disciplina, lista_professor):

    if not _validar_id(id_horario):
        return 400, "ID invalido"

    if id_horario in horarios:
        return 409, "Horario ja existe"

    if id_turma not in turmas:
        return 404, "Turma nao existe"

    if not _validar_lista(lista_disciplina):
        return 400, "Lista de disciplinas invalida"

    if not _validar_lista(lista_professor):
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
        if not _validar_lista(novas_disciplinas):
            return 400, "Lista invalida"
        horarios[id_horario]["lista_disciplina"] = novas_disciplinas

    if novos_professores is not None:
        if not _validar_lista(novos_professores):
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