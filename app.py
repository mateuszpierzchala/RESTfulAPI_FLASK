from flask import Flask, jsonify

app = Flask(__name__)
books = [
    {
        'name': 'Władca Pierścieni: Drużyna Pierścienia',
        'price': 34.50,
        'isbn':9788375062182
    },
    {
        'name': 'Lew, czarownica i stara szafa',
        'price': 19.99,
        'isbn':9788375062183
    }
]
#GET /books/9788375062182

#GET /books
@app.route('/books')
def get_books():

    return jsonify({'books':books})

@app.route ('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book["isbn"] == isbn:
            return_value = {
                'name': book["name"],
                'price': book["price"]
            }
    return jsonify(return_value)

app.run(port=5000) 