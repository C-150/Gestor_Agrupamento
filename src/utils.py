# utils.py

# ==============================
# VALIDAÇÕES GENÉRICAS
# ==============================

def validar_nome(nome):
    return isinstance(nome, str) and len(nome.strip()) > 0

def validar_email(email):
    return isinstance(email, str) and "@" in email and "." in email

def validar_numero(numero):
    return str(numero).isdigit()

def validar_id(id_horario):
    return isinstance(id_horario, str) and len(id_horario.strip()) > 0


def validar_lista(lista):
    return isinstance(lista, list)

def validar_texto(valor):
    """Verifica se é uma string não vazia (após strip)."""
    return isinstance(valor, str) and len(valor.strip()) > 0

def validar_id(valor):
    """Alias para validar_texto - usado para IDs."""
    return validar_texto(valor)

def validar_nome(valor):
    """Alias para validar_texto - usado para nomes."""
    return validar_texto(valor)

def validar_email(valor):
    """Validação simples de email: contém '@' e '.'."""
    return isinstance(valor, str) and "@" in valor and "." in valor

def validar_numero(valor):
    """Verifica se o valor pode ser convertido para inteiro (ou é um inteiro)."""
    try:
        int(valor)
        return True
    except (ValueError, TypeError):
        return False

def validar_duracao(valor):
    """Verifica se a duração é um número inteiro positivo."""
    try:
        return int(valor) > 0
    except (ValueError, TypeError):
        return False

def validar_lista(valor):
    """Verifica se é uma lista (pode estar vazia)."""
    return isinstance(valor, list)


# ==============================
# FUNÇÕES DE INPUT COM VALIDAÇÃO
# ==============================

def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: insere um número válido.")

def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Erro: texto vazio.")
