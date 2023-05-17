-- DROP DATABASE leitorcsv;
CREATE DATABASE leitorcsv;
USE leitorcsv;

CREATE TABLE expulsoes(
	id INT NOT NULL AUTO_INCREMENT,
    codigo_sancao INT NOT NULL,
	tipo_pessoa CHAR(1),
	cpf_cnpj VARCHAR(18),
	nome VARCHAR(100) NOT NULL,    
    categoria VARCHAR(100) NOT NULL,
    data_inicio DATE NULL NULL,
    data_final DATE,
    abrangencia VARCHAR(100) NOT NULL,
    cargo_efetivo VARCHAR(100) NOT NULL,
    orgao_lotacao VARCHAR(150) NOT NULL,
    orgao_sancionador VARCHAR(150),
    fundamento TEXT NOT NULL,
    PRIMARY KEY(id)
);

SELECT * FROM expulsoes;



