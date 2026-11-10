
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / "nexora.db"


def conectar():
    conexao = sqlite3.connect(DB_PATH)
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
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chave TEXT UNIQUE NOT NULL,
        valor TEXT NOT NULL
    )
    """)
    
def salvar_memoria(chave, valor):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO memorias (chave, valor)
        VALUES (?, ?)
        ON CONFLICT(chave)
        DO UPDATE SET valor = excluded.valor
        """,
        (chave, valor)
    )

    conexao.commit()
    conexao.close()
    conexao.commit()
    conexao.close()

def buscar_memoria(chave):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT valor FROM memorias WHERE chave = ?",
        (chave,)
    )

    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        return resultado[0]

    return None

def salvar_conversa(pergunta, resposta):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO conversas (pergunta, resposta) VALUES (?, ?)",
        (pergunta, resposta)
    )

    conexao.commit()
    conexao.close()
def buscar_conversas(limite=10):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT pergunta, resposta
        FROM conversas
        ORDER BY id DESC
        LIMIT ?
        """,
        (limite,)
    )

    conversas = cursor.fetchall()
    conexao.close()

    return conversas[::-1]