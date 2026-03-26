---

 📚 Sistema de Gestão de Alunos

Este projeto consiste num sistema desenvolvido em Python que permite a gestão básica de alunos organizados por turmas. A aplicação funciona através de um menu interativo no terminal, permitindo realizar operações essenciais sobre os dados.

---

🎯 Objetivo

O objetivo deste sistema é demonstrar conceitos fundamentais de programação, tais como:

* Manipulação de dicionários
* Organização de dados em estruturas hierárquicas
* Criação de funções
* Separação de responsabilidades em módulos (`aluno`, `turma`, `utils`, `main`)
* Interação com o utilizador via terminal

---

 ⚙️ Funcionalidades

O sistema inclui as seguintes operações:

* ➕ **Criar aluno** — adiciona um novo aluno a uma turma
* 📋 **Listar alunos** — apresenta todos os alunos organizados por turma
* ✏️ **Atualizar aluno** — altera o nome de um aluno existente
* 🗑️ **Remover aluno** — elimina um aluno do sistema
* ⚡ **Inserção automática** — adiciona alunos de teste (1 a 5)

---

 🗂️ Estrutura dos Dados

Os dados são armazenados em memória através de um dicionário chamado `turmas`, com a seguinte estrutura:

```python
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

🔎 **Explicação:**

* Cada turma contém vários alunos
* Cada aluno é identificado por um ID único
* A relação aluno–turma é feita através do `id_turma`

---

 🧩 Organização do Projeto

O projeto está dividido em vários ficheiros para melhor organização:

```bash
projeto/
│
├── main.py     # Interface e menu
├── aluno.py    # Operações sobre alunos
├── turma.py    # Dados das turmas
└── utils.py    # Funções de validação
```

📌 **Vantagens desta divisão:**

* Código mais limpo e organizado
* Fácil manutenção
* Reutilização de funções
* Aproximação a projetos reais

---

## 🔧 Funções Principais

### ➕ `criar_aluno()`

* Solicita ID, nome e turma
* Valida a existência da turma
* Adiciona o aluno ao sistema

---

### 📋 `listar_alunos()`

* Percorre todas as turmas
* Mostra os alunos organizados
* Indica quando não existem alunos

---

### ✏️ `atualizar_aluno()`

* Procura o aluno pelo ID
* Permite alterar o nome

---

### 🗑️ `apagar_aluno()`

* Remove um aluno com base no ID
* Garante que o aluno existe antes de apagar

---

### ⚡ `adicionar_1a5()`

* Cria automaticamente 5 alunos de teste
* Útil para demonstração rápida

---

### 🧭 `menu()`

* Apresenta opções ao utilizador
* Controla o fluxo do programa

---

### ▶️ `main()`

* Ponto de entrada do programa
* Inicia o menu interativo

---

## ▶️ Como Executar

1. Certifica-te de que tens o Python instalado
2. Coloca os ficheiros na mesma pasta
3. Executa no terminal:

```bash
python main.py
```

---

## 💡 Exemplo de Utilização

```
--- GESTOR ESCOLAR ---
1 - Criar aluno
2 - Ver alunos
3 - Atualizar aluno
4 - Apagar aluno
5 - Adicionar alunos (1 a 5)
0 - Sair
Escolhe:
```

---

## ⚠️ Limitações do Sistema

* ❗ Dados não persistentes (perdem-se ao fechar o programa)
* ❗ Apenas uma turma pré-definida
* ❗ Validação básica de dados
* ❗ Interface apenas em modo texto

---

## 🚀 Melhorias Futuras

* 💾 Guardar dados em ficheiros (JSON)
* 🏫 Criar e gerir múltiplas turmas
* 📝 Adicionar notas aos alunos
* 🔐 Melhorar validação de dados
* 🖥️ Criar interface gráfica (GUI)
* 🌐 Evoluir para aplicação web

---

## 🧠 Conceitos Aplicados

Este projeto utiliza conceitos importantes como:

* Estruturas de dados (dicionários aninhados)
* Modularização de código
* Funções e reutilização
* Entrada e saída de dados
* Controlo de fluxo (loops e condições)

---

## 👨‍💻 Autor

**Diogo Fernandes**

---
