import mysql.connector
import os
from dotenv import load_dotenv

# usar a parametrização em 100% do projeto
# endereço
# se autenticar
# enviar comandos

load_dotenv()

try:
    conexao = mysql.connector.connect(
    host= os.getenv('HOST'),
    user= os.getenv('USER'),
    password= os.getenv('PASSWORD'),
    database= os.getenv('DATABASE')
    )
    print("Conectado com sucesso!" if conexao.is_connected() else "Falha na conexão")
    cursor = conexao.cursor()

    # nas linhas abaixo onde tem cursor.execute, colocar entre aspas os comandos para o banco de teste de vocês, quando modelarmos o nosso, ai vai ficar padrão
    # cursor.execute("SELECT * FROM banco_nx.Cliente")
    cursor.execute("INSERT INTO banco_nx.Agencia (id_agencia, nome, cidade) VALUES (4, 'Agência Vila Ipojuca', 'São Paulo')")
    dados = cursor.fetchall()
    conexao.commit()

    for linha in dados:
        print(linha)
except mysql.connector.Error as erro:
    print(f"Ocorreu um erro: {erro}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()  

