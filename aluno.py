# aluno.py

from turmas import turmas
from utils import ler_int, ler_texto

def criar_aluno():
    id_aluno = ler_int("ID do aluno: ")
    nome = ler_texto("Nome: ")
    id_turma = ler_int("ID da turma: ")

    if id_turma not in turmas:
        print("Turma não existe!")
        return

    if id_aluno in turmas[id_turma]["alunos"]:
        print("Aluno já existe!")
        return

    aluno = {
        "id_aluno": id_aluno,
        "nome": nome
    }

    turmas[id_turma]["alunos"][id_aluno] = aluno
    print("Aluno criado!")

def listar_alunos():
    for turma in turmas.values():
        print(f"\nTurma {turma['nome_turma']}")
        if not turma["alunos"]:
            print("Sem alunos.")
        else:
            for a in turma["alunos"].values():
                print(f"{a['id_aluno']} - {a['nome']}")

def atualizar_aluno():
    id_aluno = ler_int("ID do aluno: ")

    for turma in turmas.values():
        if id_aluno in turma["alunos"]:
            novo_nome = ler_texto("Novo nome: ")
            turma["alunos"][id_aluno]["nome"] = novo_nome
            print("Atualizado!")
            return

    print("Aluno não encontrado.")

def apagar_aluno():
    id_aluno = ler_int("ID do aluno: ")

    for turma in turmas.values():
        if id_aluno in turma["alunos"]:
            del turma["alunos"][id_aluno]
            print("Removido!")
            return

    print("Aluno não encontrado.")

def adicionar_1a5():
    for i in range(1, 6):
        turmas[1]["alunos"][i] = {
            "id_aluno": i,
            "nome": f"Aluno{i}"
        }

    print("Alunos 1–5 adicionados!")