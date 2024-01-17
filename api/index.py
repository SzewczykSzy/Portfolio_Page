from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/projects/project_1')
def project_1():
    return render_template('project_1.html')


if __name__ == "__main__":
    app.run(debug=True)
