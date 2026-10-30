from modules.assistant import assistente_inteligente
from database.connection import criar_tabela

class NexoraAI:

    def __init__(self, nome, versao):
        self.nome = nome
        self.versao = versao

    def iniciar(self):
        print(f"\n{self.nome} - versão {self.versao}")
        print("Sistema iniciado com sucesso!")

    def exibir_menu(self):
        print("\n===== NEXORA AI =====")
        print("1 - Assistente inteligente")
        print("2 - Análise de dados")
        print("3 - Gerar relatório")
        print("0 - Sair")

    
    def executar(self):
        self.iniciar()

        while True:
            self.exibir_menu()
            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                assistente_inteligente()

            elif opcao == "2":
                print("Análise de dados selecionada!")

            elif opcao == "3":
                print("Geração de relatório selecionada!")

            elif opcao == "0":
                print("Encerrando a Nexora AI...")
                break

            else:
                print("Opção inválida. Tente novamente.")


app = NexoraAI("Nexora AI", "1.0")
criar_tabela()
app.executar()
