from database.connection import get_db_connection
from database.setup import create_tables, drop_tables

class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.name}>'
    
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
            INSERT INTO magazines (
            name, category
            ) VALUES (?, ?)
        """

        cursor.execute(sql, (self.name, self.category,))
        conn.commit()

        self.id = cursor.lastrowid


    @classmethod
    def create(cls, name, category):
        Magazine = cls(name, category)
        Magazine.save()

        return Magazine
