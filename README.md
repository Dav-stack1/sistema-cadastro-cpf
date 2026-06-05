# Sistema de Cadastro e Validação


Este projeto é uma aplicação de cadastro de clientes desenvolvida para integrar lógica de validação no backend com regras de integridade diretamente no banco de dados. O objetivo principal foi criar um fluxo de entrada de dados seguro, resiliente e focado na experiência do usuário.


## 🛠️ Arquitetura e Tecnologias


Para a construção do sistema, utilizei:

* **Python:** Criação da interface de linha de comando e validações iniciais de formato.

* **PostgreSQL:** Banco de dados relacional para persistência segura das informações.

* **DBeaver:** Ferramenta de gerenciamento visual do banco.

* **psycopg2:** Biblioteca utilizada para a comunicação nativa entre a aplicação Python e o banco de dados.


## ⚙️ Funcionalidades Principais


* **Validação de Formato:** O sistema possui um laço de repetição contínuo que orienta o usuário durante o preenchimento. Ele confere se a entrada possui os 11 dígitos numéricos necessários para um CPF válido, impedindo a inserção de strings ou caracteres soltos.

* **Integridade de Dados (Unique):** No lado do banco de dados, a tabela foi configurada com a restrição `UNIQUE` na coluna de CPF para impedir cadastros duplicados.

* **Resiliência e Tratamento de Exceções:** Para evitar crashes, foi implementado um tratamento de exceções (`try/except`) no Python. Caso um usuário tente cadastrar um documento já existente, o sistema captura a falha silenciosamente, realiza o `rollback` da transação e notifica o usuário amigavelmente para tentar novamente.
