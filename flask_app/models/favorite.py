from flask_app.config.mysqlconnection import connectToMySQL

class Favorite:
    DB = "books_schema"

    def __init__(self, data):
        self.book_id = data["book_id"]
        self.author_id = data["author_id"]