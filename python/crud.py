from python.conexao import conexao_db

# especificações: Pelo menos três consultas SELECT diferentes, incluindo pelo menos um JOIN e um WHERE. 
# Uma inserção, uma atualização e uma remoção de dados feitas via Python, todas parametrizadas (uso de %s, 
# nunca concatenando valores direto na string do comando).
# Script(s) Python com as operações pedidas (consultas, inserção, atualização, remoção) 

# listagem de tarefas por status - trazer o projeto tmb
# listagem de projetos ativos de um funcionário específico
# cadastro de tarefa
# atualização de tarefa
# delete de tarefa

# CRUD - Funcionário


def criar_funcionario(nome, cargo):
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("INSERT INTO Funcionario (Nome, Cargo) VALUES (%s, %s);",(nome, cargo))
        conectado.commit()
        print(f"Funcionário '{nome}' cadastrado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()

def listar_funcionarios():
    conectado = conexao_db()
    try:
        cursor = conectado.cursor()
        cursor.execute("SELECT ID_Funcionario, Nome, Cargo FROM Funcionario;")
        dados = cursor.fetchall()
        conectado.commit()
        for linha in dados:
            print(linha)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conectado' in locals():
            conectado.close()