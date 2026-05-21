import logging
import json
import os

from logger_config import app_logger  # noqa: F401 — garante configuracao do logger
from utils import validar_email, validar_nome, validar_numero

alunos = {}

FICHEIRO_ALUNOS = "alunos.json"


# ==============================
# PERSISTENCIA
# ==============================
def guardar_alunos():
    logging.debug("A guardar alunos no ficheiro JSON")

    try:
        with open(FICHEIRO_ALUNOS, "w", encoding="utf-8") as ficheiro:
            json.dump(alunos, ficheiro, indent=4, ensure_ascii=False)

        logging.info("Alunos guardados com sucesso")

    except Exception as erro:
        logging.error("Erro ao guardar alunos: %s", erro)


def carregar_alunos():
    global alunos

    logging.debug("Tentativa de carregar alunos")

    try:
        if os.path.exists(FICHEIRO_ALUNOS):

            with open(FICHEIRO_ALUNOS, "r", encoding="utf-8") as ficheiro:
                alunos = json.load(ficheiro)

            logging.info("Alunos carregados com sucesso")
            logging.debug("Total de alunos carregados: %s", len(alunos))

        else:
            alunos = {}
            logging.warning("Ficheiro alunos.json nao existe")

    except json.JSONDecodeError:
        logging.critical("JSON corrompido")
        alunos = {}


# ==============================
# CREATE
# ==============================
def criar_aluno(numero, nome, email, telefone, data_nascimento, id_turma):
    carregar_alunos()

    logging.debug(
        "Dados recebidos: %s %s %s",
        numero,
        nome,
        email
    )

    if not validar_numero(numero):
        logging.warning("Numero invalido: %s", numero)
        return 400, "Numero de aluno invalido"

    if not validar_nome(nome):
        logging.warning("Nome invalido para aluno %s", numero)
        return 400, "Nome invalido"

    if not validar_email(email):
        logging.warning("Email invalido para aluno %s", numero)
        return 400, "Email invalido"

    if numero in alunos:
        logging.error("Aluno %s ja existe", numero)
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

    logging.info("Aluno %s criado com sucesso", numero)

    return 201, aluno


# ==============================
# READ
# ==============================
def listar_alunos():
    carregar_alunos()

    logging.info("Listagem de alunos executada")

    if not alunos:
        logging.warning("Nenhum aluno encontrado")
        return 404, "Nenhum aluno encontrado"

    lista = []

    for aluno in alunos.values():
        lista.append(
            f"Nº: {aluno['numero_aluno']} | Nome: {aluno['nome']} | Turma: {aluno['id_turma']}"
        )

    logging.debug("Total de alunos listados: %s", len(lista))

    return 200, lista


# ==============================
# SEARCH
# ==============================
def pesquisar_aluno(texto):
    carregar_alunos()

    logging.info("Pesquisa de alunos: %s", texto)

    resultados = {}

    for num, aluno in alunos.items():

        if texto.lower() in aluno["nome"].lower() or texto in aluno["email"]:
            resultados[num] = aluno

    if not resultados:
        logging.warning("Pesquisa sem resultados: %s", texto)
        return 404, "Nenhum aluno encontrado"

    logging.info("%s alunos encontrados", len(resultados))

    return 200, resultados


# ==============================
# STATS
# ==============================
def estatisticas_alunos():
    carregar_alunos()

    total = len(alunos)

    logging.debug("Calculo de estatisticas")

    if total == 0:
        logging.warning("Sem alunos registados")
        return 404, "Sem alunos registados"

    logging.info("Estatisticas geradas")

    return 200, {
        "total_alunos": total
    }


# ==============================
# UPDATE
# ==============================
def atualizar_aluno(numero, novo_nome=None, novo_email=None):
    carregar_alunos()

    logging.info("Atualizacao do aluno %s", numero)

    if numero not in alunos:
        logging.error("Aluno %s nao encontrado", numero)
        return 404, "Aluno nao encontrado"

    if novo_nome is not None:

        if not validar_nome(novo_nome):
            logging.warning("Nome invalido para aluno %s", numero)
            return 400, "Nome invalido"

        alunos[numero]["nome"] = novo_nome

    if novo_email is not None:

        if not validar_email(novo_email):
            logging.warning("Email invalido para aluno %s", numero)
            return 400, "Email invalido"

        alunos[numero]["email"] = novo_email

    guardar_alunos()

    logging.info("Aluno %s atualizado com sucesso", numero)

    return 200, alunos[numero]


# ==============================
# DELETE
# ==============================
def apagar_aluno(numero):
    carregar_alunos()

    logging.info("Tentativa de apagar aluno %s", numero)

    if numero not in alunos:
        logging.error("Aluno %s nao encontrado", numero)
        return 404, "Aluno nao encontrado"

    aluno_eliminado = alunos[numero]

    del alunos[numero]

    guardar_alunos()

    logging.info("Aluno %s apagado com sucesso", numero)

    return 200, aluno_eliminado