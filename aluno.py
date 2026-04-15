# aluno.py

from turmas import turmas


# ==============================
# VALIDACOES
# ==============================
def _validar_nome(nome):
    return isinstance(nome, str) and len(nome.strip()) > 0

def _validar_email(email):
    return isinstance(email, str) and "@" in email and "." in email

def _validar_numero(numero):
    return str(numero).isdigit()


# ==============================
# CREATE
# ==============================
def criar_aluno(numero, nome, email, telefone, data_nascimento, id_turma):

    if not _validar_numero(numero):
        return 400, "Numero de aluno invalido"

    if not _validar_nome(nome):
        return 400, "Nome invalido"

    if not _validar_email(email):
        return 400, "Email invalido"

    if id_turma not in turmas:
        return 404, "Turma nao existe"

    if numero in turmas[id_turma]["alunos"]:
        return 409, "Aluno ja existe nesta turma"

    aluno = {
        "numero_aluno": numero,
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "data_nascimento": data_nascimento,
        "id_turma": id_turma
    }

    turmas[id_turma]["alunos"][numero] = aluno

    return 201, aluno


# ==============================
# READ
# ==============================
def listar_alunos():

    if not turmas:
        return 404, "Nao existem turmas"

    lista = []

    for turma in turmas.values():
        for aluno in turma["alunos"].values():
            lista.append(
                f"Nº: {aluno['numero_aluno']} | Nome: {aluno['nome']} | Turma: {turma['descricao']}"
            )

    if not lista:
        return 404, "Nenhum aluno encontrado"

    return 200, lista


# ==============================
# SEARCH
# ==============================
def pesquisar_aluno(texto):

    resultados = {}

    for turma in turmas.values():
        for num, aluno in turma["alunos"].items():
            if texto.lower() in aluno["nome"].lower() or texto in aluno["email"]:
                resultados[num] = aluno

    if not resultados:
        return 404, "Nenhum aluno encontrado"

    return 200, resultados


# ==============================
# STATS
# ==============================
def estatisticas_alunos():

    total = 0

    for turma in turmas.values():
        total += len(turma["alunos"])

    if total == 0:
        return 404, "Sem alunos registados"

    return 200, {
        "total_alunos": total
    }


# ==============================
# UPDATE
# ==============================
def atualizar_aluno(numero, novo_nome=None, novo_email=None):

    for turma in turmas.values():
        if numero in turma["alunos"]:

            if novo_nome is not None:
                if not _validar_nome(novo_nome):
                    return 400, "Nome invalido"
                turma["alunos"][numero]["nome"] = novo_nome

            if novo_email is not None:
                if not _validar_email(novo_email):
                    return 400, "Email invalido"
                turma["alunos"][numero]["email"] = novo_email

            return 200, turma["alunos"][numero]

    return 404, "Aluno nao encontrado"


# ==============================
# DELETE
# ==============================
def apagar_aluno(numero):

    for turma in turmas.values():
        if numero in turma["alunos"]:
            aluno_eliminado = turma["alunos"][numero]
            del turma["alunos"][numero]
            return 200, aluno_eliminado

    return 404, "Aluno nao encontrado"
