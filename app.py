from flask import Flask, json, request, Response, jsonify

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
    if ("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
        return True
    else:
        return False 


@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()
    if(validBookObject(request_data)):
        new_book = {
            "name": request_data['name'],
            "price": request_data['price'],
            "isbn": request_data['isbn']
        }

        books.insert(0,new_book)
        response = Response("", 201, mimetype='application/json')
        response.headers['Location'] = "/books/" + str(new_book['isbn'])
        return response
    else:
        invalidBookObjectErrorMsg = {
            "error":"proba przeslannia nieprawidlowego obiektu",
            "helpString": "prawidlowy format: {'name':'bookname', 'price': 7.89, 'isbn':'isbn_number'}"
        }
        response = Response(json.dumps(invalidBookObjectErrorMsg), status=400, mimetype='application/json');
        return response

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

#PUT /books/
@app.route('/books/<int:isbn>', methods = ['PUT'])
def replace_book(isbn):
    request_data = request.get_json()
    new_book = {
         'name': book["name"],
         'price': book["price"],
         'isbn': isbn
    }
    i=0;
    for book in books:
        currentIsbn = book["isbn"]
        if currentIsbn == isbn:
            books[i] = new_book
        i +=1
    response = Response("", status = 204)



app.run(port=5000) 