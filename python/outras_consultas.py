from python.conexao import conexao_db

# Pelo menos três consultas SELECT diferentes, incluindo pelo menos um JOIN e um WHERE. 

def listar_tarefa_de_projeto(situacao,id_projeto):
    """ Busca todas as tarefas de um determinado projeto, 
    que estejam com a situação determinada pelo usuário entre: (Pendente, Em Andamento, Concluída)
    Parâmetros: situacao (str)
                is_projeto (int)
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("SELECT ID_Tarefa, Descricao, Situacao FROM Tarefa WHERE Situacao = %s AND ID_Projeto = %s;", (situacao,id_projeto))
        dados = cursor.fetchall()
        conectado.commit()
        for tarefa in dados:
            id_tarefa, descricao, situacao = tarefa
            print(f"ID: {id_tarefa} | Descrição: {descricao} | Situação: {situacao}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()


def alocacoes_alta_carga_horaria_por_periodo(horas_dedicadas, data_alocacao):
    """ Busca todas as alocações com uma carga horária igual ou maior que a determinada pelo usuário, 
    e que sejam maior ou igual a data determinada pelo usuário.
    Parâmetros: horas_dedicadas (int)
                data_alocacao (date) - AAAA-MM-DD
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("SELECT ID_Alocacao, ID_Funcionario, ID_Projeto, Horas_Dedicadas, Data_Alocacao FROM Alocacao " \
                        "WHERE Horas_Dedicadas >= %s AND Data_Alocacao >= %s;", (horas_dedicadas, data_alocacao))
        dados = cursor.fetchall()
        conectado.commit()
        for alocacao in dados:
            id_alocacao, id_funcionario, id_projeto, horas_dedicadas, data_alocacao = alocacao
            print(f"ID: {id_alocacao} | ID do Funcionário: {id_funcionario} | ID do Projeto: {id_projeto} | Horas dedicadas: {horas_dedicadas} | Data da alocação: {data_alocacao}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()

def relat_de_alocacoes_com_projetos_e_funcionarios():
    """ Busca todas as alocações no banco com o nome do funcionário, nome do projeto, 
    a data e horas dedicadas.
    """
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("SELECT  a.ID_Alocacao, f.Nome AS Nome_Funcionario, p.Nome_Projeto, " \
        "DATE_FORMAT(a.Data_Alocacao, '%d/%m/%Y') AS Data_Formatada,a.Horas_Dedicadas " \
        "FROM Alocacao a " \
        "INNER JOIN Funcionario f ON a.ID_Funcionario = f.ID_Funcionario " \
        "INNER JOIN Projeto p ON a.ID_Projeto = p.ID_Projeto;")
        dados = cursor.fetchall()
        conectado.commit()
        for alocacao in dados:
            id_alocacao, nome_funcionario, nome_projeto, data_alocacao_formatada, horas_dedicadas = alocacao
            print(f"ID: {id_alocacao} | Nome do Funcionário: {nome_funcionario} | Nome do Projeto: {nome_projeto} | Data da alocação: {data_alocacao_formatada} | Horas dedicadas: {horas_dedicadas} ")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()

