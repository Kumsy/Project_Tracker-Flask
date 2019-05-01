"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template, redirect

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    
    # Get github from student_search.html form
    github = request.args.get('github')

   

    if github:
        # Unpack and get student by their github in our HB database
        first, last, github = hackbright.get_student_by_github(github)

        """
            1. Get List of project titles associated with github username.
            2. Need the grade for each project title.
            3. Return a tuple that contains the PROJECT TITLE and GRADE.
            4. Send to student_info.html the list of titles/grades.
        """
        project_tuples = hackbright.get_grades_by_github(github)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print(project_tuples)


        html = render_template("student_info.html",
                                first = first,
                                last = last,
                                github = github,
                                project_tuples = project_tuples)

        return html

    return redirect("/student_search")

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
