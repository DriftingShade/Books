from flask_app import app
from flask import flash, render_template, redirect, request, session
from flask_app.models.author import Author


@app.get("/")
def index():
    return redirect("/authors")


@app.get("/authors")
def authors():
    authors = Author.get_all_authors()
    return render_template("authors.html", authors=authors)


@app.post("/new_author")
def new_author():
    Author.create_author(request.form)
    return redirect("/authors")


@app.route("/authors/<int:author_id>")
def author_info(author_id):
    pass


# Need books and more authors in DB, author needs to add some books to favorites
# And get/display them in this route
