import psycopg2

print("Tentando conectar ao PostgreSQl...")
try:
        # 1. Estabelecendo a conexão
        conexao = psycopg2.connect(
            host = "localhost",
            database = "postgres",
            user = "postgres",
            password = "Sua senha aqui"
        )
        # 2. Criando o cursor(o nosso executor de comandos)
        cursor = conexao.cursor()
        print("Conexão realizada com sucesso!")

        # 3. Testantando uma consulta simples no banco
        cursor.execute("SELECT version();")
        versao_banco = cursor.fetchone()
        print(f"Você está conectado ao: {versao_banco[0]}")

        # 4. Fechando as portas (Boa prática!)
        cursor.close()
        conexao.close()
        print("Conexão fechada com segurança.")

except Exception as erro:
    print(f"Ops, deu erro na conexão: {erro}")