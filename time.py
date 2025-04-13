from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now()
    return f'<h1>Дата: {now.strftime("%d.%m.%Y")}</h1><h1>Текущее время: {now.strftime("%H:%M:%S")}</h1>'


if __name__ == '__main__':
    app.run()