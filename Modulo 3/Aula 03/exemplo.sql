CREATE TABLE PROFESSORES(ID INTEGER
PRIMARY KEY, NOME TEXT NOT NULL);

CREATE TABLE ALUNOS( id INTEGER
PRIMARY KEY, nome TEXT NOT NULL,
id_professor INTEGER, 
FOREIGN KEY (id_professor) REFERENCES professores(id));

INSERT INTO professores(nome) VALUES ('Anderson'), ('Paulo');

SELECT * FROM professores;

INSERT INTO alunos(nome, id_professor) VALUES('Pedro', 1), ('Maria', 2), ('José', 1);

SELECT * FROM alunos;

DELETE FROM alunos WHERE id in (4,5,6);

SELECT id AS identificador, nome, id_professor AS Registro_professor FROM alunos;

SELECT alunos.nome AS Nome_aluno, professores.nome AS Nome_professor FROM alunos
INNER JOIN professores ON alunos.id_professor = professores.id;

DROP Table alunos;