from python.conexao import conexao_db


def criar_alocacao(data_alocacao, horas_dedicadas, id_funcionario, id_projeto):
    """Cadastra uma nova alocação de um funcionário em um projeto no banco de dados.
    Parâmetros: data_alocacao (str) - AAAA-MM-DD.
                horas_dedicadas (int).
                id_funcionario (int).
                id_projeto (int).
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("INSERT INTO Alocacao (Data_Alocacao, Horas_Dedicadas, ID_Funcionario, ID_Projeto) VALUES (%s, %s, %s, %s);",(data_alocacao, horas_dedicadas, id_funcionario, id_projeto))
        conectado.commit()
        print(f"Alocação cadastrada com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()

def listar_alocacoes():
    """Lista as alocações do banco de dados.
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("SELECT ID_Alocacao, DATE_FORMAT(Data_Alocacao, '%d/%m/%Y') AS Data_Alocacao, Horas_Dedicadas, ID_Funcionario, ID_Projeto FROM Alocacao;")
        dados = cursor.fetchall()
        conectado.commit()

        for alocacao in dados:
            id_alocacao, data_alocacao, horas_dedicadas, id_funcionario, id_projeto = alocacao
            print(f"ID: {id_alocacao} | Data de Alocação: {data_alocacao} | Horas dedicadas: {horas_dedicadas} | ID do Funcionário: {id_funcionario} | ID do Projeto: {id_projeto}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()


def buscar_alocacao_por_id(id_alocacao):
    """Lista uma alocação do banco de dados.
    Parâmetros: id_Alocacao (int).
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("SELECT ID_Alocacao, DATE_FORMAT(Data_Alocacao, '%d/%m/%Y') AS Data_Alocacao, Horas_Dedicadas, ID_Funcionario, ID_Projeto FROM Alocacao WHERE ID_Alocacao = %s;", (id_alocacao,))
        dados = cursor.fetchone()
        if dados:
            id_alocacao, data_alocacao, horas_dedicadas, id_funcionario, id_projeto = dados
            print(f"ID: {id_alocacao} | Data de Alocação: {data_alocacao} | Horas dedicadas: {horas_dedicadas} | ID_Funcionário: {id_funcionario} | ID_Projeto: {id_projeto}")
        else:
            print(f"Nenhuma alocação foi encontrada com o ID {id_alocacao}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()

def atualizar_alocacao(id_alocacao, nova_data_alocacao, novas_horas_dedicadas, novo_id_funcionario, novo_id_projeto):
    """Atualiza uma alocação do banco de dados.
    Parâmetros: id_Alocacao (int).
                nova_data_alocacao (str) - AAAA-MM-DD.
                novas_horas_dedicadas (int).
                novo_id_funcionario (int).
                novo_id_projeto (int).
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("UPDATE Alocacao SET Data_Alocacao = %s, Horas_Dedicadas = %s, ID_Funcionario = %s, ID_Projeto = %s  WHERE ID_Alocacao = %s;",(nova_data_alocacao, novas_horas_dedicadas, novo_id_funcionario, novo_id_projeto,id_alocacao))
        conectado.commit()
        print("Alocação atualizada com sucesso!")
        buscar_alocacao_por_id(id_alocacao)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()


def deletar_alocacao(id_alocacao):
    """Deleta uma alocação do banco de dados.
    Parâmetros: id_Alocacao (int).
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("DELETE FROM Alocacao WHERE ID_Alocacao = %s;", (id_alocacao,))
        conectado.commit()
        print(f"Alocação {id_alocacao} deletada com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()