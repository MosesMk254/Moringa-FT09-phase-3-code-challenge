from database.connection import get_db_connection
from database.setup import create_tables
from database.setup import drop_tables

class Author:
    def __init__(self, name, id= None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.name}>'
    
    @classmethod
    def create_table(cls):
        create_tables()

    @classmethod
    def drop_table(cls):
        drop_tables()

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
            INSERT INTO authors (
            name
            ) VALUES (?)
        """

        cursor.execute(sql, (self.name,))
        conn.commit()

        self.id = cursor.lastrowid


    @classmethod
    def create(cls, name):
        Author = cls(name)
        Author.save()

        return Author
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("ID must be of type int")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) == 0:
            raise ValueError("Name must be longer than 0 characters")
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed after instantiation")
        self._name = value

    def articles(self):
        from models.article import Article
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
            SELECT articles.*
            FROM articles
            JOIN authors ON articles.author_id = authors.id
            WHERE authors.id = ?
        """
        cursor.execute(sql, (self.id,))
        article_rows = cursor.fetchall()

        articles = [Article(*row) for row in article_rows]
        return articles

    def magazines(self):
        from models.magazine import Magazine
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
            SELECT magazines.*
            FROM articles
            JOIN magazines ON articles.magazine_id = magazines.id
            JOIN authors ON articles.author_id = authors.id
            WHERE authors.id = ?
        """
        cursor.execute(sql, (self.id,))
        magazine_rows = cursor.fetchall()

        magazines = [Magazine(*row) for row in magazine_rows]
        return magazines


    



    

