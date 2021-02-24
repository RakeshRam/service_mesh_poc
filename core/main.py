import os

from flask import Flask, request, render_template, jsonify, abort
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main' # On Docker
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///main.sqlite3" # To test on local
CORS(app)

try:
    from db import db, Books
except: # TODO fix circular imports !!!
    from .db import db, Books
    
db.init_app(app)    

@app.route('/')
def index():
    return render_template('main.html', books=Books.query.all(), version=os.environ.get('VER'))

@app.route('/book/add_book/', methods=['POST'])
def add_book():
    """
    Example Request:
    ----------------
    {
        "name": "MyBook",
        "author": "John",
        "publisher": "Macmillan",
        "is_available": true
    }
    """
    content = request.get_json(silent=True)
    try:
        book = Books(**content)
        db.session.add(book)
        db.session.commit()
    except Exception as e:
        abort(400, str(e))

    return jsonify({
        'message': 'success',
        'version': os.environ.get('VER')
    })

@app.route('/book/edit_book/<int:id>/', methods=['PUT', 'DELETE'])
def edit_book(id):
    request_action = 'Update'
    # Update Book
    if request.method == 'PUT':
        content = request.get_json(silent=True)
        try:
            book = Books.query.filter_by(id=id).update(content)
            db.session.commit()
        except Exception as e:
            abort(400, str(e))

    # Delete Book
    elif request.method == 'DELETE':
        request_action = 'Delete'
        try:
            book = Books.query.get(id)
            db.session.delete(book)
            db.session.commit()
        except Exception as e:
            abort(400, str(e))
        
    return jsonify({
        'message': f'{request_action} success',
        'version': os.environ.get('VER')
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')