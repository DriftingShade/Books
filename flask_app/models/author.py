from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


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