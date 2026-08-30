from python.conexao import conexao_db


def criar_tarefa(descricao, situacao, id_projeto):
    """Cadastra uma nova tarefa no banco de dados.
    Parâmetros: descricao (str).
                situacao (str).
                id_projeto (int)
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("INSERT INTO Tarefa (Descricao,Situacao,ID_Projeto) VALUES (%s, %s, %s);",(descricao, situacao, id_projeto))
        conectado.commit()
        print(f"Tarefa cadastrada com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()

def listar_tarefas():
    """Lista as tarefas do banco de dados.
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("SELECT ID_Tarefa, Descricao, Situacao, ID_Projeto FROM Tarefa;")
        dados = cursor.fetchall()
        conectado.commit()

        for tarefa in dados:
            id_tarefa, descricao, situacao, id_projeto = tarefa
            print(f"ID: {id_tarefa} | Descrição: {descricao} | Situação: {situacao} | ID_Projeto: {id_projeto}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()


def buscar_tarefa_por_id(id_Tarefa):
    """Lista uma tarefa do banco de dados.
    Parâmetros: id_Tarefa (int).
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("SELECT ID_Tarefa, Descricao, Situacao, ID_Projeto FROM Tarefa WHERE ID_Tarefa = %s;",(id_Tarefa,))
        dados = cursor.fetchone()
        if dados:
            id_tarefa, descricao, situacao, id_projeto = dados
            print(f"ID: {id_tarefa} | Descrição: {descricao} | Situação: {situacao} | ID_Projeto: {id_projeto}")
        else:
            print(f"Nenhuma tarefa foi encontrada com o ID {id_Tarefa}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()

def atualizar_tarefa(id_Tarefa, nova_descricao, nova_situacao, id_projeto):
    """Atualiza uma tarefa do banco de dados.
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("UPDATE Tarefa SET Descricao = %s, Situacao = %s, ID_Projeto = %s WHERE ID_Tarefa = %s;",(nova_descricao, nova_situacao, id_projeto, id_Tarefa))
        conectado.commit()
        print("Dados da tarefa atualizados com sucesso!")
        buscar_tarefa_por_id(id_Tarefa)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()


def deletar_tarefa(id_Tarefa):
    """Deleta uma tarefa do banco de dados.
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("DELETE FROM Tarefa WHERE ID_Tarefa = %s;", (id_Tarefa,))
        conectado.commit()
        print(f"A tarefa de ID: {id_Tarefa} foi deletada com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()