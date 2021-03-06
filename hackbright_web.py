"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)#get student by github return a tuple
    rows = hackbright.get_grades_by_github(github)# get grades by github return a list. 

    print(rows)

    html = render_template("student_info.html",
        first = first,
        last = last,
        github = github,
        rows = rows,
        grade = rows[1],
        project_title = rows[0])         
                                                 
    return html


@app.route("/student_search")
def get_student_form():


    return render_template("student_search.html")


@app.route("/student_add")
def add_student():

    

    return render_template("student_add.html")


@app.route("/confirm_new_student", methods = ['POST'])
def confirm_new_student():

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    return render_template("confirmed_new_student.html", first_name = first_name, last_name = last_name, github = github)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
