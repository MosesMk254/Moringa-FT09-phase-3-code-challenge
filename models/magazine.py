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
        if len(value) <= 2 and len(value) >= 16:
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value