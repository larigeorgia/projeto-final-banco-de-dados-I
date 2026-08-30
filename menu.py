# from python.crud import criar_funcionario
from python.crud_projeto import criar_projeto, listar_projetos, buscar_projeto_por_id, atualizar_projeto, deletar_projeto

while True:
    print("Escolha uma das opções: ")
    print("1 - Criar Projeto")
    print("2 - Listar Projetos")
    print("3 - Buscar Projeto por ID")
    print("4 - Atualizar Projeto")
    print("5 - Deletar Projeto")
    print("0. Sair do Sistema")

    opcao = input("Digite o número da opção desejada: ").strip()

    if opcao == '0':
        print("Saindo do sistema!")
        break
    elif opcao == '1':
        nome_projeto = input("Nome do projeto: ")
        data_inicio = input("Data de início (fomato AAAA-MM-DD): ")
        criar_projeto(nome_projeto, data_inicio)

    match opcao:
        case '1':
            nome_projeto = input("Nome do projeto: ")
            data_inicio = input("Data de início (fomato AAAA-MM-DD): ")
            criar_projeto(nome_projeto, data_inicio)