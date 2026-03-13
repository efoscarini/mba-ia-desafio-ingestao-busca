from search import search_prompt

def main():
    ask = search_prompt()

    if not ask:
        print("Nao foi possivel iniciar o chat. Verifique os erros de inicializacao.")
        return

    print("Chat iniciado! Digite 'sair' para encerrar.\n")

    while True:
        pergunta = input("PERGUNTA: ").strip()

        if not pergunta:
            continue

        if pergunta.lower() == "sair":
            print("Encerrando chat. Ate logo!")
            break

        resposta = ask(pergunta)
        print(f"RESPOSTA: {resposta}\n")

if __name__ == "__main__":
    main()