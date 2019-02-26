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



# POST /books
# {
#  'name':'F',
#  'price':6.99,
#  'isbn':0123456789
#}

def validBookObject(bookObject):
    if ("name" in dictionaryObject and "price" in bookObject and "isbn" in bookObject):
        return True
    else:
        return False 


@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()
    if(validBookObject(request_data)):
       books.insert(0,request_data)
       return "True"
    else:
       return "False"

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