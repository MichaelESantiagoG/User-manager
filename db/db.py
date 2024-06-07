import random
import sqlite3 as sql
from faker import Faker

fake = Faker()

conn = sql.connect("db/users.db", check_same_thread=False)
cursor = conn.cursor()


class Usuarios_db:
    def __init__(self, Nombre, Puesto, Departamento):
        self.Nombre = Nombre
        self.Puesto = Puesto
        self.Departamento = Departamento

    def format(data):
        formated_data = {}
        for user in data:
            formated_data[user[0]] = (user[1], user[2], user[3])
        return formated_data

    def Create_Database():
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Usuarios(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Nombre TEXT,
                    Puesto TEXT,
                    Departamento TEXT);
            """
        )
        conn.commit()

    def Generate_Users(number_of_users: int):
        jobs = {
            "IT": [
                "Developer",
                "Help Desk",
                "Cloud Developer",
                "Network Engineer",
                "Cybersecurity Specialist",
            ],
            "Finance": [
                "Accountant",
                "Analyst",
                "Financial Planner",
                "Investment Banker",
                "Risk Manager",
            ],
            "Healthcare": [
                "Nurse",
                "Doctor",
                "Physical Therapist",
                "Occupational Therapist",
                "Medical Researcher",
            ],
            "Marketing": [
                "Manager",
                "Coordinator",
                "Social Media Manager",
                "Content Writer",
                "Data Analyst",
            ],
            "Sales": [
                "Representative",
                "Executive",
                "Account Manager",
                "Business Development Manager",
                "Sales Engineer",
            ],
            "Manufacturing": [
                "Engineer",
                "Operator",
                "Quality Control Inspector",
                "Supply Chain Manager",
                "Operations Researcher",
            ],
            "Education": [
                "Teacher Assistant",
                "Professor",
                "Curriculum Developer",
                "Educational Administrator",
                "Research Scientist",
            ],
            "Human Resources": [
                "HR Manager",
                "Recruiter",
                "Talent Development Specialist",
                "Compensation and Benefits Manager",
                "Diversity and Inclusion Officer",
            ],
            "Operations": [
                "Manager",
                "Coordiator",
                "Logistics Coordinator",
                "Project Manager",
                "Supply Chain Manager",
            ],
            "Consulting": [
                "Analyst",
                "Strategist",
                "Management Consultant",
                "Strategy Developer",
                "Operations Researcher",
            ],
            "Research": [
                "Scientist",
                "Investigator",
                "Data Analyst",
                "Statistical Researcher",
                "Market Researcher",
            ],
        }
        for i in range(number_of_users):
            job = random.choice(list(jobs.items()))
            user = Usuarios_db(
                Nombre=fake.first_name(),
                Departamento=job[0],
                Puesto=random.choice(job[1]),
            )
            Usuarios_db.Insert_User(user.Nombre, user.Puesto, user.Departamento)
            conn.commit()

    def Get_Users():
        return Usuarios_db.format(
            cursor.execute(
                f"""SELECT ID, Nombre, Puesto, Departamento FROM Usuarios"""
            ).fetchall()
        )

    def Get_User(user_id):
        return Usuarios_db.format(
            cursor.execute(
                f"""SELECT ID, Nombre, Puesto, Departamento FROM Usuarios WHERE ID = {user_id}"""
            ).fetchall()
        )

    def Insert_User(Nombre: str, Puesto: str, Departamento: str):
        user = Usuarios_db(
            Nombre=Nombre,
            Departamento=Departamento,
            Puesto=Puesto,
        )
        cursor.execute(
            f"""
                INSERT INTO Usuarios(Nombre, Puesto, Departamento)
                    Values('{Nombre}', '{Puesto}', '{Departamento}')"""
        )
        conn.commit()

    def Edit_User(updated_user_info: "Usuarios_db"):
        cursor.execute(
            f"""UPDATE Usuarios
                    SET Nombre='{updated_user_info.Nombre}',
                        Puesto='{updated_user_info.Puesto}',
                        Departamento='{updated_user_info.Departamento}',
                        """
        )
        conn.commit()

    def Delete_User(user_id: int):
        cursor.execute(f"""DELETE FROM Usuarios WHERE ID = {user_id}""")
        conn.commit()


# Usuarios_db.Create_Database()
# Usuarios_db.Generate_Users(30)
# print(Usuarios_db.Get_Users())
# conn.commit()

# print(Usuarios_db.Get_Users())
# print(Usuarios_db.Get_User(3))
