# curso.py

cursos = {}

from utils import validar_id , validar_nome, validar_duracao
from turmas import turmas

# ==============================
# CREATE
# ==============================
def criar_curso(id_curso, nome, descricao, duracao):

    if not validar_id(id_curso):
        return 400, "ID do curso invalido"

    if not validar_nome(nome):
        return 400, "Nome invalido"

    if not validar_duracao(duracao):
        return 400, "Duracao invalida"

    if id_curso in cursos:
        return 409, "Curso ja existe"

    # ==============================
    # ATRIBUTOS DO CURSO
    # ==============================
    curso = {
        "id_curso": id_curso,        # identificador unico
        "nome": nome,                # nome do curso
        "descricao": descricao,      # descricao do curso
        "duracao": duracao                # lista de IDs das turmas
    }

    cursos[id_curso] = curso

    return 201, curso


# ==============================
# READ
# ==============================
def listar_cursos():

    if not cursos:
        return 404, "Nenhum curso encontrado"

    lista = []

    for curso in cursos.values():
        lista.append(
            f"ID: {curso['id_curso']} | Nome: {curso['nome']} | Duracao: {curso['duracao']} | Turmas: {curso['turmas']}"
        )

    return 200, lista


# ==============================
# UPDATE
# ==============================
def atualizar_curso(id_curso, novo_nome=None, nova_duracao=None):

    if id_curso not in cursos:
        return 404, "Curso nao encontrado"

    if novo_nome is not None:
        if not validar_nome(novo_nome):
            return 400, "Nome invalido"
        cursos[id_curso]["nome"] = novo_nome

    if nova_duracao is not None:
        if not validar_duracao(nova_duracao):
            return 400, "Duracao invalida"
        cursos[id_curso]["duracao"] = nova_duracao

    return 200, cursos[id_curso]


# ==============================
# DELETE
# ==============================
def apagar_curso(id_curso):

    if id_curso not in cursos:
        return 404, "Curso nao encontrado"

    removido = cursos[id_curso]
    del cursos[id_curso]

    return 200, removido
