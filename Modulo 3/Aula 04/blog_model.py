"""
Crie a class BlogModel seguindo o exemplo da UserModel;
BlogModel deve ter os atributos:
 - conn do tipo DatabaseConnection
 - criar a tabela quando instanciado

tabela blogs:
 - id;
 - titulo;
 - conteudo;
 - data_criacao;
 - data_atualizacao;
 - id_user (chave estrangeira referente a tabela usuarios);

Faça um CRUD para:
- criar postagem
- ler todas as postagens
- ler postagens pelo id
- ler postagens pelo id_user
- atualizar postam (pelo id da postagem)
- deletar postagem (pedo id da postagem)

**Consulte o UserModel para se guiar
"""

import sqlite3
from datetime import datetime
from database import DatabaseConnection

class Blogmodel:

    def __init__(self):
        self.db_conn = DatabaseConnection()
        self._create_table()

    def _create_table(self)
                """Método privado para criar a tabela de usuários."""
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS blogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                conteudo TEXT NOT NULL,
                titulo TEXT NOT NULL UNIQUE,
                data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                id_user INTEGER,
                FOREIGN KEY (id_user) REFERENCES usuarios(id)
            );
        """
        )
        self.db_conn.close()

    def create_post(self, titulo, conteudo, id_user):
        self.db_conn.connect()
        try:
            self.db_conn.cursor.execute(
                """
                INSERT INTO blogs (titulo, conteudo, id_user)
                VALUES (?, ?, ?);
                """,
                (titulo, conteudo, id_user)
            )
            self.db_conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao criar postagem: {e}")
        finally:
            self.db_conn.close()
    
    def get_all_posts(self):
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM blogs;")
        posts = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return posts
    
    

    


        