# ==============================
# main.py
# Menu terminal - Gestor Escolar
# ==============================

from turmas import criar_turma, listar_turmas, apagar_turma
from aluno import criar_aluno, listar_alunos, atualizar_aluno, apagar_aluno

# códigos de retorno
SUCESSO = 200
ERRO_NAO_ENCONTRADO = 404
CONFLITO = 409


# menu
def menu():
    print("\n===== GESTOR ESCOLAR =====")
    print("1 - Criar aluno")
    print("2 - Listar alunos")
    print("3 - Atualizar aluno")
    print("4 - Apagar aluno")
    print("5 - Criar turma")
    print("6 - Listar turmas")
    print("7 - Apagar turma")
    print("0 - Sair")


# programa principal
def main():
    while True:
        menu()
        op = input("Escolhe uma opção: ")

        # ---------------- ALUNOS ----------------

        if op == "1":
            numero = input("Número do aluno: ")
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            data = input("Data nascimento: ")
            id_turma = input("ID da turma: ")

            return_code = criar_aluno(numero, nome, email, telefone, data, id_turma)

            if return_code[0] == SUCESSO:
                print("Aluno criado com sucesso.")
            else:
                print("Erro:", return_code[1])

        elif op == "2":
            return_code, dados = listar_alunos()

            if return_code == SUCESSO:
                print("\n--- Lista de Alunos ---")
                for aluno in dados:
                    print(aluno)
            else:
                print("Erro:", dados)

        elif op == "3":
            numero = input("Número do aluno: ")
            nome = input("Novo nome (enter para manter): ")
            email = input("Novo email (enter para manter): ")

            return_code = atualizar_aluno(
                numero,
                nome if nome else None,
                email if email else None
            )

            if return_code[0] == SUCESSO:
                print("Aluno atualizado com sucesso.")
            else:
                print("Erro:", return_code[1])

        elif op == "4":
            numero = input("Número do aluno: ")

            return_code = apagar_aluno(numero)

            if return_code[0] == SUCESSO:
                print("Aluno removido com sucesso.")
            else:
                print("Erro:", return_code[1])

        # ---------------- TURMAS ----------------

        elif op == "5":
            id_turma = input("ID da turma: ")
            descricao = input("Descrição: ")

            return_code = criar_turma(id_turma, descricao)

            if return_code[0] == SUCESSO:
                print("Turma criada com sucesso.")
            else:
                print("Erro:", return_code[1])

        elif op == "6":
            return_code, dados = listar_turmas()

            if return_code == SUCESSO:
                print("\n--- Lista de Turmas ---")
                for turma in dados:
                    print(turma)
            else:
                print("Erro:", dados)

        elif op == "7":
            id_turma = input("ID da turma: ")

            return_code = apagar_turma(id_turma)

            if return_code[0] == SUCESSO:
                print("Turma removida com sucesso.")
            else:
                print("Erro:", return_code[1])

        # ---------------- SAIR ----------------

        elif op == "0":
            print("A sair...")
            break

        else:
            print(f"{CONFLITO} - Opção inválida")


if __name__ == "__main__":
    main()
