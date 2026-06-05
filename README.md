# Sistema de Validação e Persistência de Clientes

Este é um projeto backend focado em garantir a integridade na entrada de dados de clientes e realizar a persistência segura em um banco de dados relacional. A aplicação atua como um pipeline de cadastro, validando regras de negócio e barrando dados inválidos ou duplicados antes da inserção.

## Funcionalidades

O sistema verifica a tipagem e o tamanho exato dos caracteres inseridos utilizando métodos nativos do Python, mantendo um controle de fluxo contínuo para que a aplicação rode de forma interativa durante o uso.

A gravação das informações ocorre de forma segura através da integração direta com o PostgreSQL, utilizando a biblioteca psycopg2. A modelagem da tabela no banco de dados assegura a integridade relacional com chaves incrementais automáticas (SERIAL) e restrições de duplicidade (UNIQUE).

Em caso de falhas durante a execução, o código captura as exceções e realiza o rollback das transações, protegendo a estabilidade do sistema contra interrupções abruptas.

## Tecnologias e Ambiente

O projeto foi construído utilizando Python 3 como linguagem principal. A persistência dos dados foi feita em PostgreSQL com o driver de conexão psycopg2. Todo o desenvolvimento e validação ocorreram em ambiente Linux, utilizando o PyCharm e o DBeaver.

## Como Executar

1. Clone o repositório para a sua máquina:
```bash
    git clone [https://github.com/Dav-stack1/sistema-cadastro-cpf.git](https://github.com/Dav-stack1/sistema-cadastro-cpf.git)
    ```

2. Execute o script de banco de dados no seu gerenciador (como o DBeaver) para criar a estrutura da tabela.

3. Altere as variáveis de conexão (host, database, user, password) no arquivo validador.py com as suas credenciais locais.

4. Execute a aplicação no terminal:
```bash
    python validador.py
    ```

## Estrutura do Projeto

**validador.py:** Motor principal contendo a lógica de negócio, validação e tratamento de exceções.
**teste_conexao.py:** Arquivo de teste de infraestrutura para validar o tráfego com o banco.
**banco_de_dados.sql:** Script DDL contendo a estrutura de criação da tabela.

---
Projeto construído como iniciativa pessoal para aprofundamento prático em arquitetura de dados e integração entre backend e banco de dados.

Autor: Davi Veloso (Dav-stack1)
