from flask import Flask, render_template, jsonify, request
from db import db
from threading import Thread

app = Flask(
    __name__,
    template_folder="/Users/michaelsantiago/Documents/CODES/Python/Flask API/User manager/Template",
    static_folder="/Users/michaelsantiago/Documents/CODES/Python/Flask API/User manager/Template/assets",
)


@app.route("/users/add/")
def add_user(new_user):
    query = request.args.get("Nombre", "Puesto", "Departamento")
    if query:
        return query
    # db.Usuarios_db(Nombre=new_user)


@app.route("/users/<user_id>")
def get_user(user_id):
    return db.Usuarios_db.Get_User(user_id=user_id)


@app.route("/users")
def get_all_users():
    return db.Usuarios_db.Get_Users()


@app.route("/")
def index():
    return render_template("index.html", data=db.Usuarios_db.Get_Users())


if __name__ == "__main__":
    app.run(debug=True)
