import sys
import logging

from flask import Flask, jsonify, Blueprint
from flask_cors import CORS

bp = Blueprint("Search_svc", __name__)
CORS(bp)

logger = logging.getLogger(f'App Name: Search Service - V1')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@bp.route('/search')
def search():
    # To test Search Service status.
    logger.info("Demo view to test Search Service")
    logger.debug('App Version: V1')
    data = [
        {'id':1, 'content': '<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.</p>'},
        {'id':2, 'content': '<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.</p>'},
        {'id':3, 'content': '<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.</p>'}
    ]
    logger.debug(f'Total Records: {len(data)}')
    return jsonify({'result': data, "status": 200})

app = Flask(__name__)
app.register_blueprint(bp, url_prefix='/search_svc')  # Prefix search_svc
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')