import psycopg2

try:
    # 1. Estabelecendo a conexão
    conexao = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Sua senha aqui"
    )
    # 2. Criando o cursor
    cursor = conexao.cursor()
    print("Conexão realizada com sucesso!")

except Exception as erro:
    print(f"Ops, deu erro na conexão: {erro}")
    # Se der erro aqui, o ideal seria parar o programa, mas vamos seguir.

print("---Sistema de cadastro---")

nome_cliente = input("Informe o nome do cliente: ")

while True:
    cpf = input("Informe o CPF: ")

    if len(cpf) == 11 and cpf.isnumeric():
        print(f"O CPF {cpf} passou na primeira validação!")

        bloco1 = cpf[0:3]
        bloco2 = cpf[3:6]
        bloco3 = cpf[6:9]
        final = cpf[9:11]

        print(f"CPF Formatado e salvo: {bloco1}.{bloco2}.{bloco3}-{final}")

        # O comando SQL com os 'buracos' %s
        comando_sql = "INSERT INTO clientes (nome,cpf) VALUES (%s, %s)"

        # As variáveis que vão preencher os buracos
        dados_clientes = (nome_cliente, cpf)

        try:
            # O carteiro entregando a carta pro banco
            cursor.execute(comando_sql, dados_clientes)
            conexao.commit()

            print("Dados salvos no banco de dados com sucesso!")

            cursor.close()
            conexao.close()
            break  # Sai do loop do while

        except Exception as erro:
            # Se o banco recusar (ex: CPF duplicado), ele cai aqui
            print("\nErro ao salvar: O CPF digitado já está cadastrado no sistema. Tente novamente.\n")
            conexao.rollback()  # Limpa o erro do banco

    else:
        print("Erro: CPF inválido. Tente novamente.\n")