import os
import sys
import random
import logging
import requests

from flask import Flask, request, render_template, jsonify, abort
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main' # On Docker
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///main.sqlite3" # To test on local
CORS(app)

logger = logging.getLogger(f'Custom App {os.environ.get("VER")}')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

try:
    from db import db, Books
except: # TODO fix circular imports !!!
    from .db import db, Books
    
db.init_app(app)    

@app.route('/')
def index():
    # To Stimulate 500 Internal server error.
    logger.info("Demo view to test Error handling")
    enable_retry = os.environ.get('RT')
    if enable_retry == "Y":
        c = random.choice((0,1))
        logger.warn(f"Selected Choice {c}")
        if c == 1:
            logger.error("500 Internal Server Error")
            logger.critical('Internal Server Error To Test Istio Retry Logic')
            abort(500, 'Internal Server Error To Test Istio Retry Logic')

    logger.debug(f'App Version: {os.environ.get("VER")}')
    return render_template('main.html', books=Books.query.all(), version=os.environ.get('VER'))

@app.route('/get_userinfo', methods=['GET'])
def get_userinfo():
    logger.info("Demo view to test GET API from email service")
    try:
        email_svc = f'http://{os.environ.get("email_svc")}:{os.environ.get("email_svc_port")}/email_svc/get_emails'
        logger.debug(f"EMAIL SVC: {email_svc}")
        data = requests.get(email_svc).json()
    except Exception as e:
        logger.critical(f'Error: {str(e)}')
        data = []

    logger.debug(f'Total Records: {len(data)}')
    return jsonify({'result': data, "status": 200})

@app.route('/get_search', methods=['GET'])
def get_search():
    logger.info("Demo view to test GET API from search service")
    try:
        search_svc = f'http://{os.environ.get("search_svc")}:{os.environ.get("search_svc_port")}/search_svc/search'
        logger.debug(f"SEARCH SVC: {search_svc}")
        data = requests.get(search_svc).json()
    except Exception as e:
        logger.critical(f'Error: {str(e)}')
        data = []

    logger.debug(f'Total Records: {len(data)}')
    return jsonify({'result': data, "status": 200})


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