from models.author import Author

Author.create_table()

new_author= Author.create('John Doe')