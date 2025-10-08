from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message = 'Hello Flask!', contacts = ['c1', 'c2', 'c3']);

@app.route('/blog')
def blog():
    return render_template('blog.html');


if __name__ == '__main__':

    app.run(port=80, debug=True)