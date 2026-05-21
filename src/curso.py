import logging
import json
import os

from logger_config import app_logger  # noqa: F401 — garante configuracao do logger
from utils import validar_id, validar_nome, validar_duracao

cursos = {}

FICHEIRO_CURSOS = "cursos.json"


# ==============================
# PERSISTENCIA
# ==============================
def guardar_cursos():

    logging.debug("A guardar cursos no ficheiro JSON")

    try:

        with open(FICHEIRO_CURSOS, "w", encoding="utf-8") as ficheiro:
            json.dump(cursos, ficheiro, indent=4, ensure_ascii=False)

        logging.info("Cursos guardados com sucesso")

    except Exception as erro:

        logging.error("Erro ao guardar cursos: %s", erro)


def carregar_cursos():

    global cursos

    logging.debug("Tentativa de carregar cursos")

    try:

        if os.path.exists(FICHEIRO_CURSOS):

            with open(FICHEIRO_CURSOS, "r", encoding="utf-8") as ficheiro:
                cursos = json.load(ficheiro)

            logging.info("Cursos carregados com sucesso")
            logging.debug("Total de cursos carregados: %s", len(cursos))

        else:

            cursos = {}

            logging.warning("Ficheiro cursos.json nao existe")

    except json.JSONDecodeError:

        logging.critical("JSON de cursos corrompido")

        cursos = {}


# ==============================
# CREATE
# ==============================
def criar_curso(id_curso, nome, descricao, duracao):

    carregar_cursos()

    logging.debug(
        "Dados recebidos: %s %s %s",
        id_curso,
        nome,
        duracao
    )

    if not validar_id(id_curso):

        logging.warning("ID do curso invalido: %s", id_curso)

        return 400, "ID do curso invalido"

    if not validar_nome(nome):

        logging.warning("Nome invalido para curso %s", id_curso)

        return 400, "Nome invalido"

    if not validar_duracao(duracao):

        logging.warning("Duracao invalida para curso %s", id_curso)

        return 400, "Duracao invalida"

    if id_curso in cursos:

        logging.error("Curso %s ja existe", id_curso)

        return 409, "Curso ja existe"

    curso = {
        "id_curso": id_curso,
        "nome": nome,
        "descricao": descricao,
        "duracao": duracao
    }

    cursos[id_curso] = curso

    guardar_cursos()

    logging.info("Curso %s criado com sucesso", id_curso)

    return 201, curso


# ==============================
# READ
# ==============================
def listar_cursos():

    carregar_cursos()

    logging.info("Listagem de cursos executada")

    if not cursos:

        logging.warning("Nenhum curso encontrado")

        return 404, "Nenhum curso encontrado"

    lista = []

    for curso in cursos.values():

        lista.append(
            f"ID: {curso['id_curso']} | "
            f"Nome: {curso['nome']} | "
            f"Duracao: {curso['duracao']}"
        )

    logging.debug("Total de cursos listados: %s", len(lista))

    return 200, lista


# ==============================
# UPDATE
# ==============================
def atualizar_curso(
    id_curso,
    novo_nome=None,
    nova_duracao=None
):

    carregar_cursos()

    logging.info("Atualizacao do curso %s", id_curso)

    if id_curso not in cursos:

        logging.error("Curso %s nao encontrado", id_curso)

        return 404, "Curso nao encontrado"

    if novo_nome is not None:

        if not validar_nome(novo_nome):

            logging.warning(
                "Nome invalido para curso %s",
                id_curso
            )

            return 400, "Nome invalido"

        cursos[id_curso]["nome"] = novo_nome

    if nova_duracao is not None:

        if not validar_duracao(nova_duracao):

            logging.warning(
                "Duracao invalida para curso %s",
                id_curso
            )

            return 400, "Duracao invalida"

        cursos[id_curso]["duracao"] = nova_duracao

    guardar_cursos()

    logging.info("Curso %s atualizado com sucesso", id_curso)

    return 200, cursos[id_curso]


# ==============================
# DELETE
# ==============================
def apagar_curso(id_curso):

    carregar_cursos()

    logging.info("Tentativa de apagar curso %s", id_curso)

    if id_curso not in cursos:

        logging.error("Curso %s nao encontrado", id_curso)

        return 404, "Curso nao encontrado"

    removido = cursos[id_curso]

    del cursos[id_curso]

    guardar_cursos()

    logging.info("Curso %s apagado com sucesso", id_curso)

    return 200, removido