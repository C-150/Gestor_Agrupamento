
from logger_config import app_logger  # noqa: F401 — garante configuracao do logger


# ==============================
# VALIDACOES GENERICAS
# ==============================

def validar_texto(valor):
    app_logger.debug("Validacao de texto executada")

    return isinstance(valor, str) and len(valor.strip()) > 0


def validar_id(valor):
    app_logger.debug("Validacao de ID executada: %s", valor)

    return validar_texto(valor)


def validar_nome(valor):
    app_logger.debug("Validacao de nome executada: %s", valor)

    return validar_texto(valor)


def validar_email(valor):
    app_logger.debug("Validacao de email executada: %s", valor)

    valido = (
            isinstance(valor, str)
            and "@" in valor
            and "." in valor
    )

    if not valido:
        app_logger.warning("Email invalido: %s", valor)

    return valido


def validar_numero(valor):
    app_logger.debug("Validacao de numero executada: %s", valor)

    try:

        int(valor)

        return True

    except (ValueError, TypeError):

        app_logger.exception("Numero invalido: %s", valor)

        return False


def validar_duracao(valor):
    app_logger.debug("Validacao de duracao executada: %s", valor)

    try:

        valido = int(valor) > 0

        if not valido:
            app_logger.warning("Duracao invalida: %s", valor)

        return valido

    except (ValueError, TypeError):

        app_logger.exception("Erro na validacao da duracao: %s", valor)

        return False


def validar_lista(valor):
    app_logger.debug("Validacao de lista executada")

    if not isinstance(valor, list):
        app_logger.warning("Valor recebido nao e lista")

        return False

    return True


# ==============================
# FUNCOES DE INPUT
# ==============================
def ler_int(mensagem):
    app_logger.info("Leitura de inteiro iniciada")

    while True:

        try:

            valor = int(input(mensagem))

            app_logger.info("Inteiro lido com sucesso: %s", valor)

            return valor

        except ValueError:

            app_logger.exception("Erro ao ler inteiro")

            print("Erro: insere um numero valido.")


def ler_texto(mensagem):
    app_logger.info("Leitura de texto iniciada")

    while True:

        texto = input(mensagem).strip()

        if texto:
            app_logger.info("Texto lido com sucesso")

            return texto

        app_logger.error("Texto vazio inserido")

        print("Erro: texto vazio.")
