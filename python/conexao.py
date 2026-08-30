import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv()

def conexao_db():
    try:
        conexao = mysql.connector.connect(
        host= os.getenv('HOST'),
        user= os.getenv('USER'),
        password= os.getenv('PASSWORD'),
        database= os.getenv('DATABASE')
        )
        return conexao

    except mysql.connector.Error as erro:
        print(f"Ocorreu um erro: {erro}")
