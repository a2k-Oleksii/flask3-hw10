from app import app, db
from flask import render_template, request, redirect
from models.models import Plant, Employee


@app.route("/add-plant")
def add_plant():
    plants = Plant.query.all()
    return render_template("add_plant.html", plants=plants)


@app.route("/save-plant", methods=["POST"])
def save_plant():
    name = request.form.get("name")
    location = request.form.get("location")
    plant = Plant(title=name, location=location)
    db.session.add(plant)
    db.session.commit()
    return redirect("/")


@app.route("/info-plant/<int:id>")
def info_plant(id):
    plant = Plant.query.get(id)
    employees = Employee.query.filter(Employee.plant_id == id)
    return render_template("info_plant.html", plant=plant, employees=employees)


@app.route("/delete-plant/<int:id>")
def delete_plant(id):
    plant = Plant.query.get(id)
    db.session.delete(plant)
    db.session.commit()
    return redirect("/")
