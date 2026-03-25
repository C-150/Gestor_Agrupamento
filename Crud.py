# DADOS
turmas = {
    1: {
        "id_turma": 1,
        "nome_turma": "1A",
        "alunos": {},
        "horario": []
    }
}

# FUNÇÕES CRUD ALUNOS

def criar_aluno():
    id_aluno = int(input("ID do aluno: "))
    nome = input("Nome: ")
    id_turma = int(input("ID da turma: "))

    aluno = {"id_aluno": id_aluno, "nome": nome, "id_turma": id_turma}

    if id_turma in turmas:
        turmas[id_turma]["alunos"][id_aluno] = aluno
        print("Aluno criado!")
    else:
        print("Turma não existe!")

def ler_alunos():
    for turma in turmas.values():
        print(f"\nTurma: {turma['nome_turma']}")
        for aluno in turma["alunos"].values():
            print(f"ID: {aluno['id_aluno']} | Nome: {aluno['nome']}")

def atualizar_aluno():
    id_aluno = int(input("ID do aluno a atualizar: "))

    for turma in turmas.values():
        if id_aluno in turma["alunos"]:
            novo_nome = input("Novo nome: ")
            turma["alunos"][id_aluno]["nome"] = novo_nome
            print("Aluno atualizado!")
            return

    print("Aluno não encontrado!")

def apagar_aluno():
    id_aluno = int(input("ID do aluno a apagar: "))

    for turma in turmas.values():
        if id_aluno in turma["alunos"]:
            del turma["alunos"][id_aluno]
            print("Aluno removido!")
            return

    print("Aluno não encontrado!")

# MENU
def menu():
    while True:
        print("\n--- MENU ALUNOS ---")
        print("1 - Criar aluno")
        print("2 - Ver alunos")
        print("3 - Atualizar aluno")
        print("4 - Apagar aluno")
        print("0 - Sair")

        op = input("Escolhe: ")

        if op == "1":
            criar_aluno()
        elif op == "2":
            ler_alunos()
        elif op == "3":
            atualizar_aluno()
        elif op == "4":
            apagar_aluno()
        elif op == "0":
            break
        else:
            print("Opção inválida!")

# FUNÇÃO MAIN
def main():
    menu()

# EXECUTAR
main()