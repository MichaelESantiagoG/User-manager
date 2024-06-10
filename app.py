from flask import Flask, render_template, jsonify, request
from utils import crypt
from db import db


app = Flask(
    __name__,
    template_folder="./Template",
    static_folder="./Template/assets",
)


@app.route(
    "/users/delete", methods=["DELETE"]
)  # http://127.0.0.1:5000/users/delete?id=93
def delete_user():
    user_id = request.args.get("id")
    if user_id:
        db.Usuarios_db.Delete_User(user_id)
    return f"""User #{user_id} has been permanently remove from our database"""


@app.route(
    "/users/update", methods=["PUT"]
)  # http://127.0.0.1:5000/users/update?id=93&Nombre=Michael&Puesto=API Developer&Departamento=IT
def update_user():
    user_id = request.args.get("id")
    nombre = request.args.get("Nombre")
    puesto = request.args.get("Puesto")
    departamento = request.args.get("Departamento")
    if user_id:
        try:
            db.Usuarios_db.Update_User(
                user_id=user_id, Nombre=nombre, Puesto=puesto, Departamento=departamento
            )
        except:
            return "Could not edit the user"
    return f"User #{user_id} updated succesfully"


@app.route(
    "/users/insert", methods=["POST"]
)  # http://127.0.0.1:5000/users/insert?Nombre=Nombre&Puesto=Puesto&Departamento=Departamento
def add_user():
    nombre = request.args.get("Nombre")
    puesto = request.args.get("Puesto")
    departamento = request.args.get("Departamento")
    if nombre:
        db.Usuarios_db.Insert_User(
            Nombre=nombre, Puesto=puesto, Departamento=departamento
        )
        return f"User {nombre} Added"


@app.route("/users/<user_id>", methods=["GET"])  # http://127.0.0.1:5000/users/99
def get_user(user_id):
    return db.Usuarios_db.Get_User(user_id=user_id)


@app.route("/users", methods=["GET"])  # http://127.0.0.1:5000/users
def get_all_users():
    return db.Usuarios_db.Get_Users()


data = db.Usuarios_db.Get_Users()


@app.route("/")  # http://127.0.0.1:5000
def index():
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
