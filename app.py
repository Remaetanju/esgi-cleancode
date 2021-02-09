from flask import Flask
from flask import jsonify
import user
import books

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


# USER ROUTES


@app.route('/user')
def getAllUsers():
    return jsonify(user.getall())


@app.route('/user/<who>/borrow/<title>')
def borrow(who, title):
    who = int(who)
    return jsonify(user.borrow(who, title))


@app.route('/user/<who>/giveback/<title>')
def giveback(who, title):
    who = int(who)
    return jsonify(user.giveback(who, title))


# BOOKS ROUTES


@app.route('/books/')
def getAllBooks():
    return jsonify(books.getall())


@app.route('/books/borrowed/<title>')
def borrowed(title):
    return jsonify(books.borrowable(title))


@app.route('/books/add/<who>/<title>/<author>')
def add(who, title, author):
    who = int(who)
    return jsonify(user.add(who, title, author), user.CanUserAdd(who))


# GUARD BLOCK


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
