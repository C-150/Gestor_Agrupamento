
import json

import os

from logger_config import app_logger  # noqa: F401 — garante configuracao do logger

turmas = {}

FICHEIRO_TURMAS = "turmas.json"


# ==============================
# PERSISTENCIA
# ==============================
def guardar_turmas():

    app_logger.debug("A guardar turmas no ficheiro JSON")

    try:

        with open(FICHEIRO_TURMAS, "w", encoding="utf-8") as ficheiro:
            json.dump(turmas, ficheiro, indent=4, ensure_ascii=False)

        app_logger.info("Turmas guardadas com sucesso")

    except Exception as erro:

        app_logger.exception("Erro ao guardar turmas: %s", erro)


def carregar_turmas():

    global turmas

    app_logger.debug("Tentativa de carregar turmas")

    try:

        if os.path.exists(FICHEIRO_TURMAS):

            with open(FICHEIRO_TURMAS, "r", encoding="utf-8") as ficheiro:
                turmas = json.load(ficheiro)

            app_logger.info("Turmas carregadas com sucesso")
            app_logger.debug("Total de turmas carregadas: %s", len(turmas))

        else:

            turmas = {}

            app_logger.warning("Ficheiro turmas.json nao existe")

    except json.JSONDecodeError:

        app_logger.exception("JSON de turmas corrompido")

        turmas = {}


# ==============================
# VALIDACOES
# ==============================
def validar_texto(txt):

    app_logger.debug("Validacao de texto executada")

    return isinstance(txt, str) and len(txt.strip()) > 0


# ==============================
# CREATE
# ==============================
def criar_turma(id_turma, descricao, id_curso):

    carregar_turmas()

    app_logger.debug(
        "Dados recebidos: %s %s %s",
        id_turma,
        descricao,
        id_curso
    )

    if not validar_texto(id_turma):

        app_logger.error("ID de turma invalido")

        return 400, "ID invalido"

    if not validar_texto(descricao):

        app_logger.error("Descricao invalida para turma %s", id_turma)

        return 400, "Descricao invalida"

    if id_turma in turmas:

        app_logger.error("Turma %s ja existe", id_turma)

        return 409, "Turma ja existe"

    turmas[id_turma] = {
        "id_turma": id_turma,
        "descricao": descricao,
        "horarios": [],
        "alunos": {},
        "id_curso": id_curso
    }

    guardar_turmas()

    app_logger.info("Turma %s criada com sucesso", id_turma)

    return 201, turmas[id_turma]


# ==============================
# READ
# ==============================
def listar_turmas():

    carregar_turmas()

    app_logger.info("Listagem de turmas executada")

    if not turmas:

        app_logger.error()("Nenhuma turma encontrada")

        return 404, "Nenhuma turma encontrada"

    lista = []

    for t in turmas.values():

        lista.append(
            f"ID: {t['id_turma']} | "
            f"Nome: {t['descricao']} | "
            f"Alunos: {len(t['alunos'])}"
        )

    app_logger.debug("Total de turmas listadas: %s", len(lista))

    return 200, lista


# ==============================
# SEARCH
# ==============================
def pesquisar_turma(texto):

    carregar_turmas()

    app_logger.info("Pesquisa de turma: %s", texto)

    resultados = {}

    for id_t, t in turmas.items():

        if texto.lower() in t["descricao"].lower():

            resultados[id_t] = t

    if not resultados:

        app_logger.error("Pesquisa sem resultados: %s", texto)

        return 404, "Nenhuma turma encontrada"

    app_logger.info("%s turmas encontradas", len(resultados))

    return 200, resultados


# ==============================
# STATS
# ==============================
def estatisticas_turmas():

    carregar_turmas()

    app_logger.debug("Calculo de estatisticas das turmas")

    if not turmas:

        app_logger.error("Sem turmas registadas")

        return 404, "Sem turmas registadas"

    total_turmas = len(turmas)

    total_alunos = sum(
        len(t["alunos"])
        for t in turmas.values()
    )

    app_logger.info("Estatisticas de turmas geradas")

    return 200, {
        "total_turmas": total_turmas,
        "total_alunos": total_alunos
    }


# ==============================
# UPDATE
# ==============================
def atualizar_turma(id_turma, nova_descricao):

    carregar_turmas()

    app_logger.info("Atualizacao da turma %s", id_turma)

    if id_turma not in turmas:

        app_logger.error("Turma %s nao encontrada", id_turma)

        return 404, "Turma nao encontrada"

    if not validar_texto(nova_descricao):

        app_logger.error(
            "Descricao invalida para turma %s",
            id_turma
        )

        return 400, "Descricao invalida"

    turmas[id_turma]["descricao"] = nova_descricao

    guardar_turmas()

    app_logger.info("Turma %s atualizada com sucesso", id_turma)

    return 200, turmas[id_turma]


# ==============================
# DELETE
# ==============================
def apagar_turma(id_turma):

    carregar_turmas()

    app_logger.info("Tentativa de apagar turma %s", id_turma)

    if id_turma not in turmas:

        app_logger.error("Turma %s nao encontrada", id_turma)

        return 404, "Turma nao encontrada"

    del turmas[id_turma]

    guardar_turmas()

    app_logger.info("Turma %s apagada com sucesso", id_turma)

    return 200, id_turma
