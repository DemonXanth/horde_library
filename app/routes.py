from flask import render_template, request, redirect, url_for, flash
import isbnlib
from app import app
from all import search_like, search_add, delete


@app.route('/')
@app.route('/index')
def index():
    results = search_like('ISBN', '')
    return render_template('index.html', results=results)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        results = search_like(request.form['key'], request.form['data'])
        if results == None or results == []:
            flash("No results")
            return render_template('search.html')
        else:
            return render_template('search.html', results=results)
    else:
        return render_template('search.html')


@app.route('/search/<book_id>', methods=['GET', 'POST'])
def book(book_id):
    if request.method == 'POST':
        if request.form['action'] == 'Copy':
            result = search_like("ID", book_id).pop(0)
            results = search_add(result['ISBN'])
            return redirect(url_for('book', book_id=(results.pop())['ID']))
        if request.form['action'] == 'Delete':
            delete(book_id)
            return redirect(url_for('index'))
    else:
        results = search_like('ID', book_id)
        return render_template('book.html', results=results)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        results = search_add(request.form['stupid'])
        if results == None:
            flash('That is not a valid ISBN')
            return render_template('add.html')
        else:
            return render_template('add.html', results=results)
    else:
        return render_template('add.html')
