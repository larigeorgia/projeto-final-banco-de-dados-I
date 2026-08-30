from python.crud_funcionario import criar_funcionario, listar_funcionarios, buscar_funcionario_por_id, atualizar_funcionario, deletar_funcionario
from python.crud_projeto import criar_projeto, listar_projetos, buscar_projeto_por_id, atualizar_projeto, deletar_projeto

while True:
    print(50*"=")
    print("       SISTEMA DE ALOCAÇÃO DE PROJETOS")
    print(50*"=")
    print("Escolha uma das opções: ")
    print("  \n-----FUNCIONÁRIOS-----")
    print("1 - Criar Funcionário")
    print("2 - Listar Funcionários")
    print("3 - Buscar Funcionário por ID")
    print("4 - Atualizar Funcionário")
    print("5 - Deletar Funcionário")

    print("   \n-----PROJETOS-----")
    print("6 - Criar Projeto")
    print("7 - Listar Projetos")
    print("8 - Buscar Projeto por ID")
    print("9 - Atualizar Projeto")
    print("10 - Deletar Projeto")
    print("0. Sair do Sistema")

    opcao = input("\n Digite o número da opção desejada: ").strip()

    if opcao == '0':
        print("Saindo do sistema!")
        break

    match opcao:
        case '1':
            nome_funcionario = input("Nome do funcionario: ")
            cargo = input("Cargo: ")
            criar_funcionario(nome_funcionario, cargo)
        case '2':
            listar_funcionarios()
        case '3':
            id_funcionario = int(input("Digite o ID do Funcionário:"))
            buscar_funcionario_por_id(id_funcionario)
        case '4':
            id_funcionario = int(input("Digite o ID do Funcionário:"))            
            novo_nome = input("Digite o novo nome do funcionário: ")
            novo_cargo = input("Digite o novo cargo: ")
            atualizar_funcionario(id_funcionario, novo_nome, novo_cargo)
        case '5':
            id_funcionario = int(input("Digite o ID do Funcionário:"))
            deletar_funcionario(id_funcionario)

        case '6':
            nome_projeto = input("Nome do projeto: ")
            data_inicio = input("Data de início (fomato AAAA-MM-DD): ")
            criar_projeto(nome_projeto, data_inicio)
        case '7':
            listar_projetos()
        case '8':
            id_projeto = int(input("Digite o ID do Projeto:"))
            buscar_projeto_por_id(id_projeto)
        case '9':
            id_projeto = int(input("Digite o ID do Projeto:"))            
            novo_nome = input("Digite o novo nome do projeto: ")
            nova_data = input("Digite a nova data de início (fomato AAAA-MM-DD): ")
            atualizar_projeto(id_projeto, novo_nome, nova_data)
        case '10':
            id_projeto = int(input("Digite o ID do Projeto:"))
            deletar_projeto(id_projeto)
