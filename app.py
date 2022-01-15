
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from comparisons.file_parser import file_text_to_code_string

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/"

@app.route('/')
def upload_file():
    return render_template('index.html')

@app.route('/student')
def student_page():
    return render_template('student.html')

@app.route('/teacher')
def teacher_page():
    return render_template('teacher.html')


@app.route('/display', methods = ['GET', 'POST'])
def display_file():
    if request.method == 'POST':
        prompt = request.form['prompt']
        f1 = request.files['file1']
        f2 = request.files['file2']
        filename1 = secure_filename(f1.filename)
        filename2 = secure_filename(f2.filename)

        f1.save(app.config['UPLOAD_FOLDER'] + filename1)

        file = open(app.config['UPLOAD_FOLDER'] + filename1,"r")
        content = file_text_to_code_string(file)
        
    return render_template('teacher.html', content=content) 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)