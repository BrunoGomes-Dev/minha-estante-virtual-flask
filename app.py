from flask import Flask, render_template, abort, request, redirect, url_for
from waitress import serve
from datetime import datetime
import csv

app = Flask(__name__)

def load_books():
    try:
        with open('books.csv', mode='r', encoding='utf-8') as csv_file:
            return list(csv.DictReader(csv_file))
    except:
        print("Falha ao carregar arquivo books.csv")
        return []

def save_books(new_book_data):
    fieldanames=['id', 'title', 'image_url', 'stars', 'author', 'genre','read_date', 'review']

    try:
        with open('books.csv', mode='a', encoding='utf-8', newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldanames)
            writer.writerow(new_book_data)
    except Exception as e:
        print(f"Não foi possível salvar o arquivo: {e}")

books_data = load_books()

@app.get('/')
def index():
    return render_template('index.html', books=books_data)

@app.get('/book/<int:book_id>')
def book_details(book_id):
    index = book_id - 1

    if 0 <= index <= len(books_data):
        found_book = books_data[index]
        return render_template("details.html", book=found_book)
    else:
        return abort(404, description="Livro não encontrado")

@app.get('/add')
def show_add_form():
    return render_template("add-book.html")

@app.post('/add')
def add_review():
    last_id = 0

    if len(books_data) >= 1:
        last_row = books_data[-1]

        last_id = int(last_row['id'])

    next_id = last_id + 1

    read_date_raw = request.form.get("read-date")
    date_object = datetime.strptime(read_date_raw, "%Y-%m-%d")

    formatted_date = date_object.strftime("%d/%m/%Y")

    new_book_data = {
        'id': next_id,
        'title': request.form.get("name"),
        'image_url': request.form.get("image"),
        'stars': request.form.get("rating"),
        'author': request.form.get("author"),
        'genre': request.form.get('genre'),
        'read_date': formatted_date,
        'review': request.form.get('review-text'),
    }

    save_books(new_book_data)
    books_data.append(new_book_data)

    return redirect(url_for('index'))

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000, threads=4)