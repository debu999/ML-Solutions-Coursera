from classes import Students
from classes import HighSchoolStudent

from flask import Flask, render_template, redirect, url_for, request

student_repo = []

app = Flask("flask_integrate_std")


@app.route("/", methods=["GET","POST"])
def students_page():
    if request.method == "POST":
        new_student_id = request.form.get("student-id", "")
        new_student_name = request.form.get("name", "")
        new_student_last_name = request.form.get("last-name", "")

        new_student = Students(name=new_student_name, last_name=new_student_last_name, student_id=new_student_id)
        student_repo.append(new_student)

        return redirect(url_for("students_page"))

    return render_template("index.html", student_repo=student_repo)

if __name__ == "__main__":
    app.run(debug=True)