from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.favorite import Favorite
from flask import flash


class Book:
    DB = "books_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        print(query)
        results = connectToMySQL(cls.DB).query_db(query)
        print(results)
        books = []
        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def create_book(cls, data):
        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW());"

        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def author_favorites(cls, data):
        query = """SELECT * FROM books
                JOIN favorites ON books.id = favorites.book_id
                JOIN authors ON favorites.author_id = authors.id
                WHERE authors.id = %(id)s; """
        print(query)
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        books = []
        for book in results:
            books.append(cls(book))
        return books
    
    @classmethod
    def add_fave_book(cls, data):
        query = """INSERT INTO favorites (book_id, author_id) VALUES 
        (%(book_id)s, %(author_id)s)"""
        results = connectToMySQL(Favorite.DB).query_db(query, data)
        print(results)
        return results