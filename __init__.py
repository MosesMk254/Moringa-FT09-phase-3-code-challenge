from models.author import Author
from models.magazine import Magazine

Author.drop_table()
Author.create_table()

Magazine.drop_table()
Magazine.create_table()

new_author= Author.create('John Doe')
print("Author ID:", new_author.id)
print("Author Name:", new_author.name)

new_author2 = Author.create("Jane Smith")
print("New Author ID:", new_author2.id) 
print("New Author Name:", new_author2.name)

new_author3 =Author.create('Moses Mutisya')

new_magazine=Magazine.create('Headlines', 'Breaking News')
new_magazine2= Magazine.create("Apple's secret", 'Health' )
new_magazine3 = Magazine.create('Moringa school', 'Education')