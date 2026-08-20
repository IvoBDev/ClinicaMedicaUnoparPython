#  Clínica Vida+ — Sistema de Cadastro de Pacientes

Sistema desenvolvido em **Python** para cadastro e gerenciamento básico de pacientes através do terminal.

O projeto permite cadastrar pacientes, consultar informações, listar os registros existentes e visualizar estatísticas sobre as idades dos pacientes cadastrados.

##  Funcionalidades

O sistema possui as seguintes opções:

*  **Cadastrar paciente**

  * Nome
  * Idade
  * Telefone
* **Visualizar estatísticas**

  * Total de pacientes cadastrados
  * Idade média
  * Paciente mais novo
  * Paciente mais velho
*  **Buscar paciente**

  * Busca pelo nome completo ou por parte do nome
  * Busca sem diferenciação entre letras maiúsculas e minúsculas
*  **Listar todos os pacientes cadastrados**
*  **Encerrar o sistema**

## Validações

Durante o cadastro, o sistema realiza algumas verificações para evitar entradas inválidas:

* O nome deve conter apenas letras e espaços.
* A idade deve ser um número maior que zero.
* O telefone deve possuir exatamente **11 dígitos numéricos**.
* O menu aceita apenas opções entre **1 e 5**.
* É possível cancelar o cadastro digitando `0`.

##  Tecnologias utilizadas

* **Python 3**
* Biblioteca padrão `time`

Não é necessária a instalação de bibliotecas externas.

##  Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/IvoBDev/ClinicaMedicalInoparPython.git
```

### 2. Entre na pasta do projeto

```bash
cd ClinicaMedicalInoparPython
```

### 3. Execute o programa

Caso o arquivo principal esteja nomeado como `Vida+.py`:

```bash
python "Vida+.py"
```

##  Exemplo do menu

```text
=== SISTEMA CLÍNICA VIDA+ ===

1 - Cadastrar paciente
2 - Ver estatísticas
3 - Buscar paciente
4 - Listar todos os pacientes
5 - Sair
```

##  Conceitos praticados

Durante o desenvolvimento deste projeto foram utilizados conceitos importantes de Python, como:

* Funções
* Listas
* Dicionários
* Estruturas de repetição
* Estruturas condicionais
* List comprehension
* Tratamento de exceções com `try` e `except`
* Validação de dados
* Manipulação de strings
* Entrada e saída de dados pelo terminal

##  Estrutura atual do projeto

```text
ClinicaMedicalInoparPython/
│
├── Vida+.py
└── README.md
```

##  Armazenamento dos dados

Atualmente os pacientes são armazenados em uma **lista na memória** durante a execução do programa.

Isso significa que, ao fechar o sistema, os pacientes cadastrados não ficam salvos permanentemente.


##  Autor

Desenvolvido por **Ivo Barbosa**.

Projeto criado para prática e desenvolvimento de conhecimentos em programação com Python.
