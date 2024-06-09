import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author("John Doe", 1)
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine("Tech Weekly", "Technology", 1)
        self.assertEqual(magazine.name, "Tech Weekly")

    def test_author_drop_table(self):
        Author.drop_table()
    
    def test_author_create_table(self):
        Author.create_table()

    def test_create_author_invalid_name(self):
        with self.assertRaises(ValueError):
            Author.create('')

    def test_create_author_invalid_id(self):
        with self.assertRaises(ValueError):
            Author('John Doe', id='invalid_id')

    def test_magazine_drop_table(self):
        Magazine.drop_table()

    def test_magazine_create_table(self):
        Magazine.create_table()

    def test_article_drop_table(self):
        Article.drop_table()

    def test_article_create_table(self):
        Article.create_table()

if __name__ == "__main__":
    unittest.main()
