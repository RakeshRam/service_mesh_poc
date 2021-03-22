import sys
import jwt
import logging
import datetime

from flask import Flask, jsonify, Blueprint, request, make_response
from flask_cors import CORS

bp = Blueprint("AUTH_svc", __name__)
app = Flask(__name__)
CORS(bp)

logger = logging.getLogger(f'App Name: AUTH Service - A1')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

app.config['SECRET_KEY'] = '3CC1o7xc7TwFBdLUxBQD3n4z0twlQFAhRWaAHAymoichOYz9oV'
ISSUER_CLAIM  = "admin@secure.com"

@bp.route('/get_tkn', methods=['GET']) # Should be POST
def get_tkn():
    # http://127.0.0.1:5000/auth_svc/get_tkn
    logger.info("Token Generator")
    logger.debug('App Version: A1')

    auth = request.authorization
    test_users = {
        'rakesh': 'rakesh',
        'admin': 'admin',
        'rey': 'rey'
    }
    
    if auth and auth.password == test_users.get(auth.username, "NA"):
        iat = datetime.datetime.utcnow()
        token = jwt.encode({'user' : auth.username, 'exp' : iat + datetime.timedelta(seconds=120), 
                            'iss': ISSUER_CLAIM, "iat": iat, 'sub': ISSUER_CLAIM}, 
                            app.config['SECRET_KEY'])
        return jsonify({'token' : token.decode('UTF-8')})
    
    logger.debug('UnAuthorized User')
    return make_response('UnAuthorized', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

@bp.route('/validate_tkn', methods=['GET']) # Should be POST
def validate_tkn():
    logger.info("Token Validator")
    logger.debug('App Version: A1')
    token = request.args.get('token') # http://127.0.0.1:5000/auth_svc/validate_tkn?token=eyJ0eXAiOiJKV1QiLCJhbG....

    if not token:
        logger.warn('Token is missing')
        return jsonify({'message' : 'Token is missing!'}), 401

    try: 
        data = jwt.decode(token, app.config['SECRET_KEY'])
    except:
        logger.warn('Token is InValid')
        return jsonify({'message' : 'Token is InValid!'}), 403

    logger.debug('Token is Valid')
    return jsonify({'message' : 'Valid'}), 200

app.register_blueprint(bp, url_prefix='/auth_svc')  # Prefix auth_svc
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')