CREATE TABLE autores(id INTEGER PRIMARY KEY,
nome TEXT NOT NULL, nacionalidade INTEGER);
 DROP TABLE autores;
INSERT INTO autores(nome) VALUES ('Machado'), ('Quintana');

CREATE TABLE livros(id_livro INTEGER PRIMARY KEY, titulo INTEGER NOT NULL, ano_publicacao INTEGER NOT NULL, id_autor INTEGER
FOREIGN KEY(id_autor) REFERENCES autores(id));

INSERT INTO livros(titulo)