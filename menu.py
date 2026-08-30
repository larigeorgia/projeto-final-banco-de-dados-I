from python.crud_funcionario import criar_funcionario, listar_funcionarios, buscar_funcionario_por_id, atualizar_funcionario, deletar_funcionario
from python.crud_projeto import criar_projeto, listar_projetos, buscar_projeto_por_id, atualizar_projeto, deletar_projeto
from python.crud_tarefa import criar_tarefa, listar_tarefas, buscar_tarefa_por_id, atualizar_tarefa, deletar_tarefa
from python.crud_alocacao import criar_alocacao, listar_alocacoes, buscar_alocacao_por_id, atualizar_alocacao, deletar_alocacao
from python.outras_consultas import listar_tarefa_de_projeto, alocacoes_alta_carga_horaria_por_periodo, relat_de_alocacoes_com_projetos_e_funcionarios

while True:
    print("\n"+45*"=")
    print("      SISTEMA DE ALOCAÇÃO DE PROJETOS")
    print(45*"=")
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

    print("   \n-----TAREFAS-----")
    print("11 - Criar Tarefa")
    print("12 - Listar Tarefas")
    print("13 - Buscar Tarefa por ID")
    print("14 - Atualizar Tarefa")
    print("15 - Deletar Tarefa")

    print("   \n-----ALOCAÇÕES-----")
    print("16 - Criar Alocação")
    print("17 - Listar Alocações")
    print("18 - Buscar Alocação por ID")
    print("19 - Atualizar Alocação")
    print("20 - Deletar Alocação")

    print("   \n-----OUTRAS CONSULTAS-----")
    print("21 - Listar tarefa de Projeto")
    print("22 - Alocações com alta carga horária por período")
    print("23 - Relatório de Alocações com nome de projetos e Funcionários")


    print("\n0 - Sair do Sistema")

    opcao = input("\nDigite o número da opção desejada: ").strip()

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
        case '11':
            descricao = input("Descreva a Tarefa: ")
            situacao = input("Situação da Tarefa (Pendente, Em Andamento, Concluída): ")
            id_projeto = int(input("Digite o ID do Projeto:"))
            criar_tarefa(descricao, situacao, id_projeto)
        case '12':
            listar_tarefas()
        case '13':
            id_tarefa = int(input("Digite o ID da Tarefa:"))
            buscar_tarefa_por_id(id_tarefa)
        case '14':
            id_tarefa = int(input("Digite o ID da Tarefa:"))           
            nova_descricao = input("Nova descrição da tarefa: ")
            nova_situacao = input("Nova situação da Tarefa (Pendente, Em Andamento, Concluída):")
            id_projeto = int(input("Digite o ID do Projeto:")) 
            atualizar_tarefa(id_tarefa, nova_descricao, nova_situacao, id_projeto)
        case '15':
            id_tarefa = int(input("Digite o ID da Tarefa:"))           
            deletar_tarefa(id_tarefa)
        case '16':
            data_alocacao = input("Data da alocação (fomato AAAA-MM-DD): ")
            horas_dedicadas = int(input("Digite a quantidade de horas que serão dedicadas ao projeto:"))
            id_funcionario = int(input("Digite o ID do Funcionário:"))
            id_projeto = int(input("Digite o ID do Projeto:"))
            criar_alocacao(data_alocacao, horas_dedicadas, id_funcionario, id_projeto)
        case '17':
            listar_alocacoes()
        case '18':
            id_alocacao = int(input("Digite o ID da Alocação:"))
            buscar_alocacao_por_id(id_alocacao)
        case '19':
            id_alocacao = int(input("Digite o ID da Alocação:"))
            nova_data_alocacao = input("Nova data da alocação (fomato AAAA-MM-DD): ")
            novas_horas_dedicadas = int(input("Nova quantidade de horas que serão dedicadas ao projeto:"))
            novo_id_funcionario = int(input("Novo ID do Funcionário:"))
            novo_id_projeto = int(input("Novo ID do Projeto:")) 
            atualizar_alocacao(id_alocacao, nova_data_alocacao, novas_horas_dedicadas, novo_id_funcionario, novo_id_projeto)
        case '20':
            id_alocacao = int(input("Digite o ID da Alocação:"))
            deletar_alocacao(id_alocacao)
        case '21':
            situacao = input("Situação da Tarefa (Pendente, Em Andamento, Concluída): ")
            id_projeto = int(input("Digite o ID do Projeto:"))
            listar_tarefa_de_projeto(situacao, id_projeto)
        case '22':
            horas_dedicadas = int(input("Digite a quantidade de horas para análise:"))
            data_alocacao = input("Digite a partir de qual data será feito o filtro (fomato AAAA-MM-DD, exemplo: 2026-08-01): ")
            alocacoes_alta_carga_horaria_por_periodo(horas_dedicadas, data_alocacao)
        case '23':
            relat_de_alocacoes_com_projetos_e_funcionarios()
