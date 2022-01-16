from re import L

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from comparisons.comparison_funcs import compare_submission_solution, is_passing
from comparisons.file_parser import file_text_to_code_string
from comparisons.student_functions import StudentFunctions

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/"


@app.route("/")
def upload_file():
    return render_template("index.html")


@app.route("/student")
def student_page():
    return render_template("student.html")


@app.route("/teacher")
def teacher_page():
    return render_template("teacher.html")


@app.route("/teacher_results", methods=["GET", "POST"])
def display_file():
    if request.method == "POST":
        starter = request.files["starter"]
        f1 = request.files["file1"]
        f2 = request.files["file2"]

        starter_text = file_text_to_code_string(starter)
        submission = file_text_to_code_string(f1)
        solution = file_text_to_code_string(f2)
        results = is_passing(
            compare_submission_solution(starter_text, submission, solution)
        )

    return render_template("results_teacher.html", content=results)


@app.route("/student_results", methods=["GET", "POST"])
def student_stuff():
    if "submit_button" in request.form:
        user_answer = request.form["functions"]

    if request.files["student_file"]:
        code = request.files["student_file"]
        code_text = file_text_to_code_string(code)

        result = {
            "fix": lambda code_text: StudentFunctions().fix_code(code_text),
            "time": lambda code_text: StudentFunctions().get_time_complexity(code_text),
            "docstring": lambda code_text: StudentFunctions().get_python_docstring(
                code_text
            ),
            "stream": lambda code_text: StudentFunctions().convert_loop_to_python_stream(
                code_text
            ),
            "list": lambda code_text: StudentFunctions().convert_list_comprehension_to_loop(
                code_text
            ),
            "loop": lambda code_text: StudentFunctions().convert_loop_to_list_comprehension(
                code_text
            ),
        }[user_answer](code_text)

        print(user_answer)

    return render_template("results_student.html", content=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
