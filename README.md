# 📚 Gestor Escolar (Python)

Sistema simples de gestão escolar em Python, utilizando o padrão CRUD (Create, Read, Update, Delete).

---

## 🎯 Funcionalidades

O sistema permite gerir:

* 👨‍🎓 Alunos
* 🏫 Turmas
* 📘 Cursos
* 🗓️ Horários

Tudo através de um menu no terminal.

---

## 📁 Estrutura do Projeto

```
main.py
aluno.py
turmas.py
curso.py
horario.py
```

---

## 🧠 Conceitos Utilizados

* Dicionários (armazenamento em memória)
* Funções
* Validações simples
* CRUD
* Organização modular

---

## ⚙️ Como Executar

1. Abrir o terminal
2. Executar:

```
python main.py
```

---

## 🧾 Funcionalidades por Módulo

### 👨‍🎓 Alunos

* Criar aluno
* Listar alunos
* Atualizar aluno
* Apagar aluno

---

### 🏫 Turmas

* Criar turma
* Listar turmas
* Apagar turma

---

### 📘 Cursos

**Atributos:**

* `id_curso`
* `nome`
* `descricao`
* `duracao`
* `turmas` (lista de IDs)

**Funcionalidades:**

* Criar curso
* Listar cursos
* Atualizar curso
* Apagar curso

---

### 🗓️ Horários

**Atributos:**

* `id_horario`
* `id_turma`
* `lista_disciplina`
* `lista_professor`

**Exemplo:**

```
{
  "id_horario": "H1",
  "id_turma": "T1",
  "lista_disciplina": ["matematica", "portugues"],
  "lista_professor": ["prof1", "prof2"]
}
```

**Funcionalidades:**

* Criar horário
* Listar horários
* Atualizar horário
* Apagar horário

---

## 📌 Notas

* Os dados são guardados apenas em memória (não existe base de dados)
* Ao fechar o programa, os dados são perdidos
* Sistema desenvolvido para fins educativos

---

## 👨‍💻 Autor

Diogo Fernandes
