
import requests
from database.connection import salvar_memoria

from database.connection import (
    salvar_conversa,
    criar_tabela,
    buscar_conversas,
    buscar_memoria
)


def assistente_inteligente():

    print("\n===== NEXORA AI =====")
    print("Converse com a Nexora. Digite 'sair' para encerrar.\n")

    historico = []

    conversas_anteriores = buscar_conversas()
    nome = buscar_memoria("nome")

    for pergunta_antiga, resposta_antiga in conversas_anteriores:
        historico.append(f"Usuário: {pergunta_antiga}")
        historico.append(f"Nexora: {resposta_antiga}")

    if nome:
        historico.append(
            f"Informação importante: o nome do usuário é {nome}."
        )

    while True:

        pergunta = input("Você: ")

        if pergunta.lower() == "sair":
            print("Nexora: Até a próxima!")
            break
        if pergunta.lower().startswith("meu nome é "):
             nome = pergunta[11:].strip().rstrip(".!?")

        if nome:
            salvar_memoria("nome", nome)
            historico.append(
                f"Informação importante: o nome do usuário é {nome}."
        )

        historico.append(f"Usuário: {pergunta}")
        historico = historico[-20:]

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
            historico = historico[-20:]

            salvar_conversa(pergunta, texto)

        except requests.exceptions.RequestException as erro:
            print(f"\nErro na comunicação com a IA: {erro}")
