
import requests
from database.connection import salvar_conversa
from database.connection import criar_tabela
from database.connection import buscar_conversas

def assistente_inteligente():

    print("\n===== NEXORA AI =====")
    print("Converse com a Nexora. Digite 'sair' para encerrar.\n")

    historico = []

    conversas_anteriores = buscar_conversas()

    for pergunta_antiga, resposta_antiga in conversas_anteriores:
        historico.append(f"Usuário: {pergunta_antiga}")
        historico.append(f"Nexora: {resposta_antiga}")

    while True:

        pergunta = input("Você: ")

        if pergunta.lower() == "sair":
            print("Nexora: Até a próxima!")
            break

        historico.append(f"Usuário: {pergunta}")

        contexto = "\n".join(historico)

        try:
            resposta = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "qwen2.5:3b",
                    "prompt": f"""
                    Você é a Nexora, uma assistente inteligente.
                    Seja educada, clara e objetiva.

                    Histórico da conversa:
                    {contexto}

                    Responda à última pergunta do usuário.
                    """,
                    "stream": False
                },
                timeout=180
            )

            resposta.raise_for_status()

            texto = resposta.json()["response"]

            print(f"\nNexora: {texto}\n")

            historico.append(f"Nexora: {texto}")

            salvar_conversa(pergunta, texto)

        except requests.exceptions.RequestException as erro:
            print(f"\nErro na comunicação com a IA: {erro}")

