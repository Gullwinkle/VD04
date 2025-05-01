from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'link': 'Подробнее'
    }
    return render_template('home.html', **context)


@app.route('/blog/')
def blog():
    return render_template('blog.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run()