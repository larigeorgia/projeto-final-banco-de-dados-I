from conexao import conexao_db

# especificações: Pelo menos três consultas SELECT diferentes, incluindo pelo menos um JOIN e um WHERE. 
# Uma inserção, uma atualização e uma remoção de dados feitas via Python, todas parametrizadas (uso de %s, 
# nunca concatenando valores direto na string do comando).
# Script(s) Python com as operações pedidas (consultas, inserção, atualização, remoção) 

# listagem de tarefas por status - trazer o projeto tmb
# listagem de projetos ativos de um funcionário específico

# cadastro de tarefa
# atualização de tarefa
# delete de tarefa

def consulta():
    conectado = conexao_db()
    if conectado is None:
        return []
    print(conectado)
    try:
        cursor = conectado.cursor()

        cursor.execute("SELECT * FROM banco_nx.Cliente")
        # cursor.execute("INSERT INTO banco_nx.Agencia (id_agencia, nome, cidade) VALUES (4, 'Agência Vila Ipojuca', 'São Paulo')")
        # return cursor.fetchall()
        dados = cursor.fetchall()
        conectado.commit()

        for linha in dados:
            print(linha)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conectado.close()

# consulta()

def criar_cliente(id_cliente, nome, id_endereco_cliente):
    conectado = conexao_db()

    if conectado is None:
        return False
    
    try:
        cursor = conectado.cursor()
        # query = cursor.execute("SELECT * FROM banco_nx.Cliente")
        # cursor.execute(query)
        # cursor.execute("SELECT * FROM banco_nx.Cliente")
        
        cursor.execute("INSERT INTO banco_nx.Cliente (id_cliente, nome, id_endereco_cliente) VALUES (%s, %s, %s)", (id_cliente, nome, id_endereco_cliente))
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
 
criar_cliente(3, 'Maria Oliveira', 2)