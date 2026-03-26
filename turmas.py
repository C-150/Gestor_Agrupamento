# turma.py

turmas = {
    1: {
        "id_turma": 1,
        "nome_turma": "1A",
        "alunos": {}
    }
}

def listar_turmas():
    for turma in turmas.values():
        print(f"ID: {turma['id_turma']} | Nome: {turma['nome_turma']}")