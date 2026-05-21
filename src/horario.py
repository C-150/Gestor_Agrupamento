import json
import os

from logger_config import app_logger  # noqa: F401 — garante configuracao do logger
from turmas import turmas
from utils import validar_id, validar_lista

horarios = {}

FICHEIRO_HORARIOS = "horarios.json"


# ==============================
# PERSISTENCIA
# ==============================
def guardar_horarios():

    app_logger.debug("A guardar horarios no ficheiro JSON")

    try:
        with open(FICHEIRO_HORARIOS, "w", encoding="utf-8") as ficheiro:
            json.dump(horarios, ficheiro, indent=4, ensure_ascii=False)

        app_logger.info("Horarios guardados com sucesso")

    except Exception as erro:
        app_logger.exception("Erro ao guardar horarios: %s", erro)


def carregar_horarios():

    global horarios

    app_logger.debug("Tentativa de carregar horarios")

    try:

        if os.path.exists(FICHEIRO_HORARIOS):

            with open(FICHEIRO_HORARIOS, "r", encoding="utf-8") as ficheiro:
                horarios = json.load(ficheiro)

            app_logger.info("Horarios carregados com sucesso")
            app_logger.debug("Total de horarios carregados: %s", len(horarios))

        else:
            horarios = {}
            app_logger.error("Ficheiro horarios.json nao existe")

    except json.JSONDecodeError:

        app_logger.exception("JSON de horarios corrompido")
        horarios = {}


# ==============================
# CREATE
# ==============================
def criar_horario(
    id_horario,
    id_turma,
    lista_disciplina,
    lista_professor
):

    carregar_horarios()

    app_logger.debug(
        "Dados recebidos: %s %s",
        id_horario,
        id_turma
    )

    if not validar_id(id_horario):
        app_logger.error("ID de horario invalido: %s", id_horario)
        return 400, "ID invalido"

    if id_horario in horarios:
        app_logger.error("Horario %s ja existe", id_horario)
        return 409, "Horario ja existe"

    if id_turma not in turmas:
        app_logger.error("Turma %s nao existe", id_turma)
        return 404, "Turma nao existe"

    if not validar_lista(lista_disciplina):
        app_logger.error(
            "Lista de disciplinas invalida no horario %s",
            id_horario
        )
        return 400, "Lista de disciplinas invalida"

    if not validar_lista(lista_professor):
        app_logger.error(
            "Lista de professores invalida no horario %s",
            id_horario
        )
        return 400, "Lista de professores invalida"

    horario = {
        "id_horario": id_horario,
        "id_turma": id_turma,
        "lista_disciplina": lista_disciplina,
        "lista_professor": lista_professor
    }

    horarios[id_horario] = horario

    guardar_horarios()

    app_logger.info("Horario %s criado com sucesso", id_horario)

    return 201, horario


# ==============================
# READ
# ==============================
def listar_horarios():

    carregar_horarios()

    app_logger.info("Listagem de horarios executada")

    if not horarios:
        app_logger.error("Nenhum horario encontrado")
        return 404, "Nenhum horario encontrado"

    lista = []

    for h in horarios.values():

        lista.append(
            f"ID: {h['id_horario']} | "
            f"Turma: {h['id_turma']} | "
            f"Disciplinas: {h['lista_disciplina']}"
        )

    app_logger.debug("Total de horarios listados: %s", len(lista))

    return 200, lista


# ==============================
# UPDATE
# ==============================
def atualizar_horario(
    id_horario,
    novas_disciplinas=None,
    novos_professores=None
):

    carregar_horarios()

    app_logger.info("Atualizacao do horario %s", id_horario)

    if id_horario not in horarios:
        app_logger.error("Horario %s nao encontrado", id_horario)
        return 404, "Horario nao encontrado"

    if novas_disciplinas is not None:

        if not validar_lista(novas_disciplinas):
            app_logger.error(
                "Lista de disciplinas invalida no horario %s",
                id_horario
            )
            return 400, "Lista invalida"

        horarios[id_horario]["lista_disciplina"] = novas_disciplinas

    if novos_professores is not None:

        if not validar_lista(novos_professores):
            app_logger.error(
                "Lista de professores invalida no horario %s",
                id_horario
            )
            return 400, "Lista invalida"

        horarios[id_horario]["lista_professor"] = novos_professores

    guardar_horarios()

    app_logger.info("Horario %s atualizado com sucesso", id_horario)

    return 200, horarios[id_horario]


# ==============================
# DELETE
# ==============================
def apagar_horario(id_horario):

    carregar_horarios()

    app_logger.info("Tentativa de apagar horario %s", id_horario)

    if id_horario not in horarios:
        app_logger.error("Horario %s nao encontrado", id_horario)
        return 404, "Horario nao encontrado"

    removido = horarios[id_horario]

    del horarios[id_horario]

    guardar_horarios()

    app_logger.info("Horario %s apagado com sucesso", id_horario)

    return 200, removido
