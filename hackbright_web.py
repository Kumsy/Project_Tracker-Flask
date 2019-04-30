"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    
    # Get github from student_search.html form
    github = request.args.get('github')

    # Unpack and get student by their github in our HB database
    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
                            first = first,
                            last = last,
                            github = github)

    return html

@app.route("/student_search")
def get_student_form():
    """ Show form for searching for a student"""

    return render_template("student_search.html")

@app.route("/student_add")
def add_student_form():
    """ Show form for searching for a student"""

    return render_template("student_add.html")

@app.route("/student_added", methods=["POST"])
def student_add():

    first_name = request.form.get('first')
    last_name = request.form.get('last')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    return render_template("student_added.html", 
        first_name = first_name,
        last_name = last_name,
        github = github)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
