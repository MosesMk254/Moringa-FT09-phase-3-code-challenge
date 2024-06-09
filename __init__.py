from models.author import Author
from models.magazine import Magazine
from models.article import Article

Author.drop_table()
Author.create_table()

Magazine.drop_table()
Magazine.create_table()

Article.drop_table()
Article.create_table()

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

new_article = Article.create('People', 'Education', new_author, new_magazine)
new_article2 = Article.create('School', 'Moringa', new_author3, new_magazine2)
new_article3 = Article.create('Taste', 'Food', new_author2, new_magazine3)
print('New Article Id:', new_article.id)
print('New Article Id:', new_article2.id)
print('New Article Title:', new_article2)

print('Article Aurthor', new_article3.author().name)
print('Article Aurthor', new_article.magazine().name)