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

    match opcao:
        case '1':
            nome_projeto = input("Nome do projeto: ")
            data_inicio = input("Data de início (fomato AAAA-MM-DD): ")
            criar_projeto(nome_projeto, data_inicio)
            
        case '2':
            listar_projetos()
            
        case '3':
            id_projeto = int(input("Digite o ID do Projeto:"))
            buscar_projeto_por_id(id_projeto)
            
        case '4':
            id_projeto = int(input("Digite o ID do Projeto:"))            
            novo_nome = input("Digite o novo nome do projeto: ")
            nova_data = input("Digite a nova data de início (fomato AAAA-MM-DD): ")
            atualizar_projeto(id_projeto, novo_nome, nova_data)
            
        case '5':
            id_projeto = int(input("Digite o ID do Projeto:"))
            deletar_projeto(id_projeto)
