from models.author import Author

Author.drop_table()
Author.create_table()

new_author= Author.create('John Doe')
print("Author ID:", new_author.id)
print("Author Name:", new_author.name)

new_author2 = Author.create("Jane Smith")
print("New Author ID:", new_author2.id) 
print("New Author Name:", new_author2.name)

new_author3 =Author.create('Moses Mutisya')