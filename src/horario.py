import logging
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

    logging.debug("A guardar horarios no ficheiro JSON")

    try:
        with open(FICHEIRO_HORARIOS, "w", encoding="utf-8") as ficheiro:
            json.dump(horarios, ficheiro, indent=4, ensure_ascii=False)

        logging.info("Horarios guardados com sucesso")

    except Exception as erro:
        logging.error("Erro ao guardar horarios: %s", erro)


def carregar_horarios():

    global horarios

    logging.debug("Tentativa de carregar horarios")

    try:

        if os.path.exists(FICHEIRO_HORARIOS):

            with open(FICHEIRO_HORARIOS, "r", encoding="utf-8") as ficheiro:
                horarios = json.load(ficheiro)

            logging.info("Horarios carregados com sucesso")
            logging.debug("Total de horarios carregados: %s", len(horarios))

        else:
            horarios = {}
            logging.warning("Ficheiro horarios.json nao existe")

    except json.JSONDecodeError:

        logging.critical("JSON de horarios corrompido")
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

    logging.debug(
        "Dados recebidos: %s %s",
        id_horario,
        id_turma
    )

    if not validar_id(id_horario):
        logging.warning("ID de horario invalido: %s", id_horario)
        return 400, "ID invalido"

    if id_horario in horarios:
        logging.error("Horario %s ja existe", id_horario)
        return 409, "Horario ja existe"

    if id_turma not in turmas:
        logging.error("Turma %s nao existe", id_turma)
        return 404, "Turma nao existe"

    if not validar_lista(lista_disciplina):
        logging.warning(
            "Lista de disciplinas invalida no horario %s",
            id_horario
        )
        return 400, "Lista de disciplinas invalida"

    if not validar_lista(lista_professor):
        logging.warning(
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

    logging.info("Horario %s criado com sucesso", id_horario)

    return 201, horario


# ==============================
# READ
# ==============================
def listar_horarios():

    carregar_horarios()

    logging.info("Listagem de horarios executada")

    if not horarios:
        logging.warning("Nenhum horario encontrado")
        return 404, "Nenhum horario encontrado"

    lista = []

    for h in horarios.values():

        lista.append(
            f"ID: {h['id_horario']} | "
            f"Turma: {h['id_turma']} | "
            f"Disciplinas: {h['lista_disciplina']}"
        )

    logging.debug("Total de horarios listados: %s", len(lista))

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

    logging.info("Atualizacao do horario %s", id_horario)

    if id_horario not in horarios:
        logging.error("Horario %s nao encontrado", id_horario)
        return 404, "Horario nao encontrado"

    if novas_disciplinas is not None:

        if not validar_lista(novas_disciplinas):
            logging.warning(
                "Lista de disciplinas invalida no horario %s",
                id_horario
            )
            return 400, "Lista invalida"

        horarios[id_horario]["lista_disciplina"] = novas_disciplinas

    if novos_professores is not None:

        if not validar_lista(novos_professores):
            logging.warning(
                "Lista de professores invalida no horario %s",
                id_horario
            )
            return 400, "Lista invalida"

        horarios[id_horario]["lista_professor"] = novos_professores

    guardar_horarios()

    logging.info("Horario %s atualizado com sucesso", id_horario)

    return 200, horarios[id_horario]


# ==============================
# DELETE
# ==============================
def apagar_horario(id_horario):

    carregar_horarios()

    logging.info("Tentativa de apagar horario %s", id_horario)

    if id_horario not in horarios:
        logging.error("Horario %s nao encontrado", id_horario)
        return 404, "Horario nao encontrado"

    removido = horarios[id_horario]

    del horarios[id_horario]

    guardar_horarios()

    logging.info("Horario %s apagado com sucesso", id_horario)

    return 200, removido