import logging
from logger_config import app_logger  # noqa: F401 — garante configuracao do logger


# ==============================
# VALIDACOES GENERICAS
# ==============================

def validar_texto(valor):
    logging.debug("Validacao de texto executada")

    return isinstance(valor, str) and len(valor.strip()) > 0


def validar_id(valor):
    logging.debug("Validacao de ID executada: %s", valor)

    return validar_texto(valor)


def validar_nome(valor):
    logging.debug("Validacao de nome executada: %s", valor)

    return validar_texto(valor)


def validar_email(valor):
    logging.debug("Validacao de email executada: %s", valor)

    valido = (
            isinstance(valor, str)
            and "@" in valor
            and "." in valor
    )

    if not valido:
        logging.warning("Email invalido: %s", valor)

    return valido


def validar_numero(valor):
    logging.debug("Validacao de numero executada: %s", valor)

    try:

        int(valor)

        return True

    except (ValueError, TypeError):

        logging.warning("Numero invalido: %s", valor)

        return False


def validar_duracao(valor):
    logging.debug("Validacao de duracao executada: %s", valor)

    try:

        valido = int(valor) > 0

        if not valido:
            logging.warning("Duracao invalida: %s", valor)

        return valido

    except (ValueError, TypeError):

        logging.warning("Erro na validacao da duracao: %s", valor)

        return False


def validar_lista(valor):
    logging.debug("Validacao de lista executada")

    if not isinstance(valor, list):
        logging.warning("Valor recebido nao e lista")

        return False

    return True


# ==============================
# FUNCOES DE INPUT
# ==============================
def ler_int(mensagem):
    logging.info("Leitura de inteiro iniciada")

    while True:

        try:

            valor = int(input(mensagem))

            logging.info("Inteiro lido com sucesso: %s", valor)

            return valor

        except ValueError:

            logging.error("Erro ao ler inteiro")

            print("Erro: insere um numero valido.")


def ler_texto(mensagem):
    logging.info("Leitura de texto iniciada")

    while True:

        texto = input(mensagem).strip()

        if texto:
            logging.info("Texto lido com sucesso")

            return texto

        logging.warning("Texto vazio inserido")

        print("Erro: texto vazio.")