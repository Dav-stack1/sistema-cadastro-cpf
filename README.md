# Cadastro e Validação de CPF

Fiz esse projeto para treinar a integração do Python com o PostgreSQL e aplicar regras de validação e tratamento de erros na prática.

A ideia é bem direta: um script de terminal que recebe um CPF, faz a validação do formato (se tem 11 dígitos e se são apenas números) e tenta salvar no banco de dados.

Para evitar dados duplicados, a tabela do Postgres tem uma restrição `UNIQUE` no CPF. No lado do Python, coloquei blocos `try/except`. Se o usuário digitar um documento que já existe, o script captura a falha, faz o rollback no banco e pede o número de novo, tudo sem "crashar" o programa no meio da execução.

## O que usei
- Python 3
- PostgreSQL (gerenciado pelo DBeaver)
- Biblioteca `psycopg2` para conectar o Python ao banco

## Como testar na sua máquina

1. Clone este repositório.
2. Rode o comando que está no arquivo `banco_de_dados.sql` no seu banco para criar a tabela.
3. Abra o arquivo `validador.py` e troque as informações de conexão (usuário e senha) pelas do seu banco local.
4. Rode o script no terminal:
```bash
   python validador.py
