from flask_app import app
from flask import flash, render_template, redirect, request, session
from flask_app.models.author import Author
from flask_app.models.book import Book


@app.get("/books")
def books():
    books = Book.get_all_books()
    return render_template("books.html", books=books)

@app.post("/books/new_book")
def new_book():
    Book.create_book(request.form)
    return redirect("/books")

@app.post("/books/add_favorite")
def fave_book():
    author_id = request.form["author_id"]
    book_id = request.form["book_id"]
    Book.add_fave_book(book_id, author_id)
    return redirect(f"/authors/{author_id}")