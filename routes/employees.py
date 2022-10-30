from app import app, db
from flask import render_template, request, redirect
from models.models import Employee


@app.route("/add-employee")
def add_Employees():
    employees = Employee.query.all()
    return render_template("add_employee.html", employees=employees)


@app.route("/save-employee", methods=["POST"])
def save_employee():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    plant_id = request.form.get("plant_id")
    employee = Employee(first_name=first_name, last_name=last_name, plant_id=plant_id)
    db.session.add(employee)
    db.session.commit()
    return redirect("/")


# @app.route("/info-plant/<int:id>")
# def info_plant(id):
#     plant = Plant.query.get(id)
#     employees = Employee.query.filter(Employee.plant_id == id)
#     return render_template("info_plant.html", plant=plant, employees=employees)


@app.route("/delete-employee/<int:id>")
def delete_employee(id):
    employee = Employee.query.get(id)
    db.session.delete(employee)
    db.session.commit()
    return redirect("/")
