from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/faculty')
def faculty():
    return render_template('faculty.html')


@app.route('/programs')
def programs():
    return render_template('programs.html')


@app.route('/courses')
def courses():
    return render_template('courses.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)

