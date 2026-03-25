# 📚 Sistema de Gestão de Alunos

Este projeto é um sistema simples em Python para gerir alunos dentro de turmas. Permite criar, visualizar, atualizar e apagar alunos através de um menu interativo no terminal.

---

## 🚀 Funcionalidades

O sistema inclui as seguintes operações:

* ✅ Criar aluno
* 📖 Listar alunos
* ✏️ Atualizar dados de um aluno
* ❌ Remover aluno

---

## 🗂️ Estrutura dos Dados

Os dados são armazenados em um dicionário chamado `turmas`, com a seguinte estrutura:

```
turmas = {
    id_turma: {
        "id_turma": int,
        "nome_turma": str,
        "alunos": {
            id_aluno: {
                "id_aluno": int,
                "nome": str,
                "id_turma": int
            }
        },
        "horario": []
    }
}
```

---

## 🧩 Funções Principais

### `criar_aluno()`

* Solicita ID, nome e turma
* Adiciona o aluno à turma existente

### `ler_alunos()`

* Mostra todos os alunos organizados por turma

### `atualizar_aluno()`

* Permite alterar o nome de um aluno existente

### `apagar_aluno()`

* Remove um aluno com base no ID

### `menu()`

* Interface principal com opções interativas

### `main()`

* Função principal que inicia o programa

---

## ▶️ Como Executar

1. Certifique-se de ter o Python instalado
2. Guarde o código num ficheiro, por exemplo:
   `gestao_alunos.py`
3. Execute no terminal:

```
python gestao_alunos.py
```

---

## 💡 Exemplo de Uso

```
MENU ALUNOS
1 - Criar aluno
2 - Ver alunos
3 - Atualizar aluno
4 - Apagar aluno
0 - Sair
Escolhe: 1
```

---

## ⚠️ Notas

* Apenas existe uma turma inicial (`1A`)
* IDs devem ser únicos (não há validação automática)
* Os dados não são guardados permanentemente (não usa ficheiros ou base de dados)

---

## 🔧 Melhorias Futuras

* Guardar dados em ficheiro (JSON ou base de dados)
* Validar entradas do utilizador
* Permitir criar novas turmas
* Interface gráfica (GUI)

---

## 👨‍💻 Autor

Diogo Fernandes

---
