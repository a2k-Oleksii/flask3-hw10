from app import app
from flask import render_template
from models.models import Plant, Employee


@app.route("/")
def main():
    plants = Plant.query.all()
    employees = Employee.query.all()
    return render_template("index.html", plants=plants, employees=employees)
