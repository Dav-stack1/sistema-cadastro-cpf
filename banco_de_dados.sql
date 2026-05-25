create table clientes (
    id SERIAL PRIMARY key,
    nome VARCHAR(100) not null,
    cpf VARCHAR(11) not null unique,
    data_cadastro timestamp default CURRENT_TIMESTAMP
);