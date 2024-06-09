from database.connection import get_db_connection
from database.setup import create_tables, drop_tables

class Article:
    def __init__(self, title, content, author_id, magazine_id, id=None):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f'<Article {self.title}>'


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
            INSERT INTO articles (
            title, content, author_id, magazine_id
            ) VALUES (?, ?, ?, ?)
        """

        cursor.execute(sql, (self.title, self.content, self.author_id, self.magazine_id,))
        conn.commit()

        self.id = cursor.lastrowid

    @classmethod
    def create(cls, title, content, author, magazine):
        article = cls(title, content, author.id, magazine.id)
        article.save()

        return article

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("ID must be of type int")
        self._id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string")
        if not 5 <= len(value) <= 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, str):
            raise ValueError("Content must be a string")
        if hasattr(self, '_content'):
            raise AttributeError("Article cannot be changed after instantiation")
        self._content = value

    def author(self):
        from models.author import Author
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
            SELECT authors.*
            FROM articles
            JOIN authors ON articles.author_id = authors.id
            WHERE articles.id = ?
        """
        cursor.execute(sql, (self.id,))
        author_row = cursor.fetchone()

        if author_row:
            author = Author(name=author_row['name'], id=author_row['id'])
            return author
        else:
            return None

    def magazine(self):
        from models.magazine import Magazine
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
            SELECT magazines.*
            FROM articles
            JOIN magazines ON articles.magazine_id = magazines.id
            WHERE articles.id = ?
        """
        cursor.execute(sql, (self.id,))
        magazine_row = cursor.fetchone()

        if magazine_row:
            magazine = Magazine(name=magazine_row['name'], category=magazine_row['category'], id=magazine_row['id'])
            return magazine
        else:
            return None
