from flask import render_template, request
import isbnlib
from app import app
from all import search_like, getCoverSmall


@app.route('/')
@app.route('/index')
def index():
    results = search_like('ISBN', '')
    return render_template('index.html', results=results)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        results = search_like(request.form['key'], request.form['data'])
        return render_template('search.html', results=results)
    else:
        return render_template('search.html')
