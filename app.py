import markdown
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/main')
def All():
    return render_template('main.html')


@app.route('/historia')
def historia():  # put application's code here
    file = open('./static/Polska 17w.md', 'r')
    md_template_string = markdown.markdown(file.read())
    return md_template_string


@app.route('/biologia')
def biologia():  # put application's code here
    return render_template('biologia.html')


if __name__ == '__main__':
    app.run()
