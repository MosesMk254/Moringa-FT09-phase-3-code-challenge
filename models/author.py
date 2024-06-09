from database.connection import get_db_connection
from database.setup import create_tables

class Author:
    def __init__(self, name, id= None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.name}>'
    
    @classmethod
    def create_table(cls):
        create_tables()

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



    

