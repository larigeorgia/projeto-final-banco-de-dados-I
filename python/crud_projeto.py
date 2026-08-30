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
        cursor.execute("SELECT ID_Projeto, Nome_Projeto, Data_Inicio FROM Projeto;")
        dados = cursor.fetchall()
        conectado.commit()
        for projeto in dados:
            print(projeto)
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
        cursor.execute("SELECT ID_Projeto, Nome_Projeto, Data_Inicio FROM Projeto WHERE ID_Projeto = %s;",(id_Projeto))
        dados = cursor.fetchone()
        conectado.commit()
        print(dados)
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
        cursor.execute("DELETE FROM Projeto WHERE ID_Projeto = %s;", (id_Projeto))
        conectado.commit()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()