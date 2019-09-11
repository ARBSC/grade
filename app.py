from flask import Flask, render_template, url_for, request, jsonify
from api import get_json_data


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/search/<search>', methods=['GET'])
def search_info(search):
    
    # pass search to api and return render template with info
    results = get_json_data(search.upper())
    if results:
        return render_template('cards.html', data=results), 200
    else:
        return render_template('search_404.html'), 400
    #jsonify(results)
    

if __name__ == '__main__':
    app.run(debug=True)

