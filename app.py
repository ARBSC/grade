from api import my_list
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/cards')
def cards():
    return render_template('cards.html', data=my_list)

@app.route('/')
def index():
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)
