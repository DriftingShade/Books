from flask_app.config.mysqlconnection import connectToMySQL


class Author:
    DB = "books_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        print(query)
        results = connectToMySQL(cls.DB).query_db(query)
        print(results)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def create_author(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"

        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def find_author_by_id(cls, data):

        query = "SELECT * FROM authors WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        return results[0]

    @classmethod
    def fave_books(cls, data):
        query = """SELECT * FROM authors
                JOIN favorites ON authors.id = favorites.author_id
                JOIN books ON favorites.book_id = books.id
                WHERE books.id = %(id)s; """
        print(query)
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def not_favorite_authors(cls, data):
        query = """SELECT * FROM authors WHERE authors.id 
        NOT IN (SELECT author_id FROM favorites WHERE book_id = %(id)s);"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def add_fave_author(cls, data):
        query = """INSERT INTO favorites (book_id, author_id) VALUES 
        (%(book_id)s, %(author_id)s)"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        return results
