from time import sleep

pacientes = []


# Opção 1 - Função Cadastrar Paciente
def cadastro():
    # 1. Nome
    while True:
        nome = input("Nome do Paciente: ").strip()

        if nome == "0":
            print("\033[33mCadastro cancelado!\033[0m")
            return

        if nome.replace(" ", "").isalpha():
            break

        print("\033[31mERRO! Tente novamente ou digite zero para voltar ao menu inicial.\033[0m")

    # 2. Idade
    while True:
        try:
            idade = int(input("Idade: "))

            if idade == 0:
                print("\033[33mCadastro cancelado!\033[0m")
                return

            if idade > 0:
                break

            print("\033[31mErro: A idade deve ser maior que zero!\033[0m")

        except ValueError:
            print("\033[31mErro: Digite uma idade válida (apenas números)!\033[0m")

    # 3. Telefone
    while True:
        telefone = input("Telefone (11 dígitos): ").strip()

        if telefone == "0":
            print("\033[33mCadastro cancelado!\033[0m")
            return

        if len(telefone) == 11 and telefone.isdigit():
            break

        print("\033[31mErro: O telefone deve conter exatamente 11 dígitos numéricos!\033[0m")

    # Salvando os dados
    sleep(0.5)

    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    }

    pacientes.append(paciente)

    print("\033[32m\nCadastro efetuado com sucesso!\033[0m")
    sleep(1)


# Opção 2 - Função Exibir Estatísticas
def estatisticas():
    if not pacientes:
        print("\033[31m\nNenhum paciente cadastrado ainda.\033[0m")
        sleep(1.5)
        return

    idades = [p["idade"] for p in pacientes]

    total_pacientes = len(idades)
    media = sum(idades) / total_pacientes

    # Considera inicialmente o primeiro paciente
    # como o mais novo e o mais velho
    mais_novo = pacientes[0]
    mais_velho = pacientes[0]

    # Percorre a lista comparando as idades
    for paciente in pacientes:
        if paciente["idade"] < mais_novo["idade"]:
            mais_novo = paciente

        if paciente["idade"] > mais_velho["idade"]:
            mais_velho = paciente

    print("=" * 27)
    print("ESTATÍSTICAS DOS PACIENTES")
    print("=" * 27)

    print(f"Pacientes cadastrados: {total_pacientes}")
    print(f"Idade média: {media:.1f} anos")
    print(f"Paciente mais novo: {mais_novo['nome']} - {mais_novo['idade']} anos")
    print(f"Paciente mais velho: {mais_velho['nome']} - {mais_velho['idade']} anos")

    sleep(2)


# Opção 3 - Função Buscar Paciente
# Busca Parcial e Insensível a Maiúsculas
def buscar_paciente():
    if not pacientes:
        print("\033[31mBase de dados sem pacientes cadastrados.\033[0m")
        sleep(1.5)
        return

    termo_busca = input(
        "\nDigite o nome (ou parte do nome) do paciente: "
    ).strip().lower()

    if not termo_busca:
        print("\033[31mO termo de busca não pode ser vazio.\033[0m")
        return

    # Filtra todos os pacientes que contêm o termo buscado no nome
    encontrados = [
        p for p in pacientes
        if termo_busca in p["nome"].lower()
    ]

    if encontrados:
        print("=" * 35)
        print(f"RESULTADOS DA BUSCA ({len(encontrados)} encontrado(s))")
        print("=" * 35)

        for paciente in encontrados:
            print(f"Nome: {paciente['nome']}")
            print(f"Idade: {paciente['idade']}")
            print(f"Telefone: {paciente['telefone']}")
            print("-" * 35)

    else:
        print("\033[31m\nNenhum paciente encontrado com esse nome!\033[0m")

    sleep(2)


# Opção 4 - Função Listar Todos os Pacientes
def listar_pacientes():
    if not pacientes:
        print("\033[31m\nNenhum paciente cadastrado para listar.\033[0m")
        sleep(1.5)
        return

    print("=" * 35)
    print("LISTA DE PACIENTES CADASTRADOS")
    print("=" * 35)

    for i, p in enumerate(pacientes, start=1):
        print(
            f"{i}. Nome: {p['nome']} | "
            f"Idade: {p['idade']} | "
            f"Tel: {p['telefone']}"
        )

    sleep(2)


# Menu - Programa Principal
while True:
    print("""\033[33m

=== SISTEMA CLÍNICA VIDA+ ===

1 - Cadastrar paciente
2 - Ver estatísticas
3 - Buscar paciente
4 - Listar todos os pacientes
5 - Sair

\033[0m""")

    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao < 1 or opcao > 5:
            print("\033[31mOpção inválida! Escolha um número de 1 a 5.\033[0m")
            continue

    except ValueError:
        print("\033[31mErro: Digite apenas números entre 1 e 5!\033[0m")
        continue

    if opcao == 1:
        cadastro()

    elif opcao == 2:
        estatisticas()

    elif opcao == 3:
        buscar_paciente()

    elif opcao == 4:
        listar_pacientes()

    elif opcao == 5:
        print("\033[33mSaindo do sistema... Até logo!\033[0m")
        break
