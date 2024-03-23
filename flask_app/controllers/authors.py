from flask_app import app
from flask import flash, render_template, redirect, request, session
from flask_app.models.author import Author
from flask_app.models.book import Book


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


@app.post("/authors/add_favorite")
def fave_author():
    data = {"book_id": request.form["id"], "author_id": request.form["author_id"]}
    book_id = request.form["id"]
    Author.add_fave_author(data)
    return redirect(f"/books/{book_id}")


@app.get("/authors/<int:author_id>")
def author_info(author_id):
    author = Author.find_author_by_id({"id": author_id})
    if author == None:
        return "Could Not Find Author!"
    fave_books = Book.author_favorites({"id": author_id})
    not_faves = Book.not_favorite_books({"id": author_id})
    return render_template(
        "author_show.html",
        author=author,
        not_faves=not_faves,
        fave_books=fave_books,
    )
