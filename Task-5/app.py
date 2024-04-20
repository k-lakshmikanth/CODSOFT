import flask
import pandas as pd
from datetime import datetime
from hashlib import new
import sqlite3

generate_id = lambda:new("sha256", datetime.now().isoformat().encode()).hexdigest()

app = flask.Flask("contacts")

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/list")
def list():
    with sqlite3.connect("data/contacts.db") as cursor:
        data = cursor.execute("SELECT id, Name, PhoneNumber, Email, Address FROM contacts")
    return flask.render_template("list.html", contacts=data.fetchall())

@app.route("/search", methods=["get", "post"])
def search():
    if flask.request.method == "POST":
        search = flask.request.form["search"]
        category = flask.request.form["category"]
        with sqlite3.connect("data/contacts.db") as conn:
            data = conn.cursor().execute(f"SELECT id, Name, PhoneNumber, Email, Address FROM contacts where {category} like '%{search}%'")
        return flask.render_template("list.html", contacts=data.fetchall())
    return flask.render_template("search.html")

@app.route("/add", methods=["get", "post"])
def add():
    if flask.request.method == "POST":
        id = generate_id()
        name = flask.request.form["name"]
        email = flask.request.form["email"]
        phone = flask.request.form["phone"]
        address = flask.request.form["address"]
        with sqlite3.connect("data/contacts.db") as conn:
            conn.cursor().execute(f"insert into contacts(id, Name, Email, PhoneNumber, Address) values ('{id}','{name}', '{email}', {phone}, '{address}')")
        return flask.redirect("/")
    return flask.render_template("add.html")

@app.route("/update/<id>", methods=["get", "post"])
def update(id):
    if flask.request.method == "POST":
        name = flask.request.form["name"]
        email = flask.request.form["email"]
        phone = flask.request.form["phone"]
        address = flask.request.form["address"]
        with sqlite3.connect("data/contacts.db") as conn:
            conn.cursor().execute(f"update contacts set Name='{name}', Email='{email}', PhoneNumber={phone}, Address='{address}' where id='{id}'")
        return flask.redirect("/")

    with sqlite3.connect("data/contacts.db") as conn:
        data = conn.cursor().execute(f"SELECT * FROM contacts where id = '{id}'").fetchall()[0]
    return flask.render_template("update.html", contact=data)

@app.route("/delete/<id>")
def delete(id):
    with sqlite3.connect("data/contacts.db") as conn:
        conn.cursor().execute(f"delete from contacts where id='{id}'")
    return flask.redirect("/list")

if __name__ == "__main__":
    app.run(debug=True)