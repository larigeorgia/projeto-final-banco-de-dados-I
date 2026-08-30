from python.conexao import conexao_db


def criar_funcionario(nome, cargo):
    """Cadastra um novo funcionario no banco de dados.
    Parâmetros: nome (str).
                cargo (str)..
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("INSERT INTO Funcionario (Nome,Cargo) VALUES (%s, %s);",(nome, cargo))
        conectado.commit()
        print(f"Funcionário {nome} cadastrado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()

def listar_funcionarios():
    """Lista os funcionarios do banco de dados.
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("SELECT ID_Funcionario, Nome, Cargo FROM Funcionario;")
        dados = cursor.fetchall()
        conectado.commit()

        for funcionario in dados:
            id_funcionario, nome, cargo = funcionario
            print(f"ID: {id_funcionario} | Nome: {nome} | Cargo: {cargo}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()


def buscar_funcionario_por_id(id_Funcionario):
    """Lista um funcionário do banco de dados.
    Parâmetros: id_Funcionario (int).
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("SELECT ID_Funcionario, Nome, Cargo FROM Funcionario WHERE ID_Funcionario = %s;",(id_Funcionario,))
        dados = cursor.fetchone()
        if dados:
            id_funcionario, nome, cargo = dados
            print(f"ID: {id_funcionario} | Nome: {nome} | Cargo: {cargo}")
        else:
            print(f"Nenhum projeto foi encontrado com o ID {id_funcionario}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()

def atualizar_funcionario(id_Funcionario, novo_nome_funcionario, novo_cargo):
    """Atualiza um funcionário do banco de dados.
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("UPDATE Funcionario SET Nome = %s, Cargo = %s WHERE ID_Funcionario = %s;",(novo_nome_funcionario, novo_cargo, id_Funcionario))
        conectado.commit()
        print("Dados do funcionário atualizados com sucesso!")
        buscar_funcionario_por_id(id_Funcionario)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()


def deletar_funcionario(id_Funcionario):
    """Deleta um funcionário do banco de dados.
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("DELETE FROM Funcionario WHERE ID_Funcionario = %s;", (id_Funcionario,))
        conectado.commit()
        print(f"Funcionario {id_Funcionario} deletado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()