from python.conexao import conexao_db


def criar_projeto(nome_projeto, data_inicio):
    """Cadastra um novo projeto no banco de dados.
    Parâmetros: nome_projeto (str).
                data_inicio (str) - AAAA-MM-DD.
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("INSERT INTO Projeto (Nome_Projeto,Data_Inicio) VALUES (%s, %s);",(nome_projeto, data_inicio))
        conectado.commit()
        print(f"Projeto {nome_projeto} cadastrado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()

def listar_projetos():
    """Lista os projetos do banco de dados.
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("SELECT ID_Projeto, Nome_Projeto, DATE_FORMAT(Data_Inicio, '%d/%m/%Y') AS Data_Inicio FROM Projeto;")
        dados = cursor.fetchall()
        conectado.commit()

        for projeto in dados:
            id_projeto, nome_projeto, data_inicio = projeto
            print(f"ID: {id_projeto} | Projeto: {nome_projeto} | Data de Início: {data_inicio}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()


def buscar_projeto_por_id(id_Projeto):
    """Lista um projeto do banco de dados.
    Parâmetros: id_Projeto (int).
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("SELECT ID_Projeto, Nome_Projeto, DATE_FORMAT(Data_Inicio, '%d/%m/%Y') AS Data_Inicio FROM Projeto WHERE ID_Projeto = %s;",(id_Projeto,))
        dados = cursor.fetchone()
        if dados:
            id_projeto, nome_projeto, data_inicio = dados
            print(f"ID: {id_projeto} | Projeto: {nome_projeto} | Data de Início: {data_inicio}")
        else:
            print(f"Nenhum projeto foi encontrado com o ID {id_projeto}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()

def atualizar_projeto(id_Projeto, novo_nome_projeto, nova_data_inicio):
    """Atualiza um projeto do banco de dados.
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("UPDATE Projeto SET Nome_Projeto = %s, Data_Inicio = %s WHERE ID_Projeto = %s;",(novo_nome_projeto, nova_data_inicio, id_Projeto))
        conectado.commit()
        print("Projeto atualizado com sucesso!")
        buscar_projeto_por_id(id_Projeto)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()


def deletar_projeto(id_Projeto):
    """Deleta um projeto do banco de dados.
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("DELETE FROM Projeto WHERE ID_Projeto = %s;", (id_Projeto,))
        conectado.commit()
        print(f"Projeto {id_Projeto} deletado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()