
import sqlite3


def conectar():
    conexao = sqlite3.connect("data/nexora.db")
    return conexao


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pergunta TEXT NOT NULL,
            resposta TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()
def salvar_conversa(pergunta, resposta):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO conversas (pergunta, resposta) VALUES (?, ?)",
        (pergunta, resposta)
    )

    conexao.commit()
    conexao.close()
def buscar_conversas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT pergunta, resposta FROM conversas ORDER BY id"
    )

    conversas = cursor.fetchall()
    conexao.close()

    return conversas