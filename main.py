# main.py

from aluno import (
    criar_aluno,
    listar_alunos,
    atualizar_aluno,
    apagar_aluno,
    adicionar_1a5
)

def menu():
    while True:
        print("\n--- GESTOR ESCOLAR ---")
        print("1 - Criar aluno")
        print("2 - Ver alunos")
        print("3 - Atualizar aluno")
        print("4 - Apagar aluno")
        print("5 - Adicionar alunos (1 a 5)")
        print("0 - Sair")

        op = input("Escolhe: ")

        if op == "1":
            criar_aluno()
        elif op == "2":
            listar_alunos()
        elif op == "3":
            atualizar_aluno()
        elif op == "4":
            apagar_aluno()
        elif op == "5":
            adicionar_1a5()
        elif op == "0":
            break
        else:
            print("Opção inválida!")

def main():
    menu()

if __name__ == "__main__":
    main()