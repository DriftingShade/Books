from flask_app import app
from flask import flash, render_template, redirect, request, session
from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app.controllers import books


@app.get("/")
def index():
    return redirect("/authors")


@app.get("/authors")
def authors():
    authors = Author.get_all_authors()
    return render_template("authors.html", authors=authors)


@app.post("/authors/new_author")
def new_author():
    Author.create_author(request.form)
    return redirect("/authors")


@app.get("/authors/<int:author_id>")
def author_info(author_id):
    author = Author.find_author_by_id({"id": author_id})
    fave_books = Book.author_favorites({"id": author_id})
    book_list = Book.get_all_books()
    if author == None:
        return "Could Not Find Author!"
    return render_template("author_show.html", author=author, fave_books=fave_books, book_list=book_list)
