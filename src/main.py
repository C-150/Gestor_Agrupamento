# ==============================
# main.py
# Menu terminal - Gestor Escolar
# ==============================
from curso import criar_curso, listar_cursos, atualizar_curso, apagar_curso
from turmas import criar_turma, listar_turmas, apagar_turma
from aluno import criar_aluno, listar_alunos, atualizar_aluno, apagar_aluno
from horario import criar_horario, listar_horarios, atualizar_horario, apagar_horario

# códigos de retorno
SUCESSO = 200
CREATE = 201
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
    print("8 - Criar curso")
    print("9 - Listar cursos")
    print("10 - Atualizar curso")
    print("11 - Apagar curso")
    print("12 - Criar horario")
    print("13 - Listar horarios")
    print("14 - Atualizar horario")
    print("15 - Apagar horario")
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

            if return_code[0] == CREATE:
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

        elif op == "12":
            id_turma = input("ID da turma: ")

        # ---------------- CURSOS ----------------

        elif op == "8":
            id_curso = input("ID do curso: ")
            nome = input("Nome: ")
            descricao = input("Descricao: ")
            duracao = input("Duracao: ")

            return_code = criar_curso(id_curso, nome, descricao, duracao)

            if return_code[0] == CREATE:
                print("Curso criado com sucesso.")
            else:
                print("Erro:", return_code[1])


        elif op == "9":
            return_code, dados = listar_cursos()

            if return_code == SUCESSO:
                print("\n--- Lista de Cursos ---")
                for curso in dados:
                    print(curso)
            else:
                print("Erro:", dados)


        elif op == "10":
            id_curso = input("ID do curso: ")

            nome = input("Novo nome (enter para manter): ")
            duracao = input("Nova duracao (enter para manter): ")

            return_code = atualizar_curso(
                id_curso,
                nome if nome else None,
                duracao if duracao else None
            )

            if return_code[0] == SUCESSO:
                print("Curso atualizado com sucesso.")
            else:
                print("Erro:", return_code[1])


        elif op == "11":
            id_curso = input("ID do curso: ")

            return_code = apagar_curso(id_curso)

            if return_code[0] == SUCESSO:
                print("Curso removido com sucesso.")
            else:
                print("Erro:", return_code[1])

        # ---------------- HORARIOS ----------------

        elif op == "12":
            id_horario = input("ID do horario: ")
            id_turma = input("ID da turma: ")

            disciplinas_input = input("Disciplinas (separadas por virgula): ")
            professores_input = input("Professores (separados por virgula): ")

            lista_disciplina = disciplinas_input.split(",")
            lista_professor = professores_input.split(",")

            return_code = criar_horario(id_horario, id_turma, lista_disciplina, lista_professor)

            if return_code[0] == CREATE:
                print("Horario criado com sucesso.")
            else:
                print("Erro:", return_code[1])


        elif op == "13":
            return_code, dados = listar_horarios()

            if return_code == SUCESSO:
                print("\n--- Lista de Horarios ---")
                for h in dados:
                    print(h)
            else:
                print("Erro:", dados)


        elif op == "14":
            id_horario = input("ID do horario: ")

            disciplinas_input = input("Novas disciplinas (enter para manter): ")
            professores_input = input("Novos professores (enter para manter): ")

            novas_disciplinas = disciplinas_input.split(",") if disciplinas_input else None
            novos_professores = professores_input.split(",") if professores_input else None

            return_code = atualizar_horario(id_horario, novas_disciplinas, novos_professores)

            if return_code[0] == SUCESSO:
                print("Horario atualizado com sucesso.")
            else:
                print("Erro:", return_code[1])


        elif op == "15":
            id_horario = input("ID do horario: ")

            return_code = apagar_horario(id_horario)

            if return_code[0] == SUCESSO:
                print("Horario removido com sucesso.")
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
