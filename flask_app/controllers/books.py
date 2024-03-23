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
    data = {"author_id": request.form["id"], "book_id": request.form["book_id"]}
    author_id = request.form["id"]
    Book.add_fave_book(data)
    return redirect(f"/authors/{author_id}")


@app.get("/books/<int:book_id>")
def find_book(book_id):
    book = Book.find_book_by_id({"id": book_id})
    if book == None:
        return "Could Not Find Book!"
    fave_authors = Author.fave_books({"id": book_id})
    not_faves = Author.not_favorite_authors({"id": book_id})
    return render_template(
        "book_show.html", book=book, fave_authors=fave_authors, not_faves=not_faves
    )
