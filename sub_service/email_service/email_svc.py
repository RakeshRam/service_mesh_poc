import os
import sys
import random
import logging

from flask import Flask, request, render_template, jsonify, abort
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)

CORS(app)

logger = logging.getLogger(f'App Name: Email Service - {os.environ.get("VER")}')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.route('/test')
def index():
    # To test Email Service status.
    logger.info("Demo view to test Email Service")
    logger.debug(f'App Version: V1')

    return jsonify({'result': "UP", "status": 200})

@app.route('/send_email', methods=['POST'])
def send_email():
    logger.info("Demo view to test Email Notification Status")
    user_id = request.get_json(silent=True)
    c = random.choice((0,1))
    email_status = False
    if c == int(user_id):
        email_status = True

    logger.debug(f'Email Notification Status: {email_status}')
    return jsonify({'result': email_status, "status": 200})

@app.route('/get_emails', methods=['GET'])
def get_emails():
    logger.info("Demo view to get email address of users")
    data = [
        {'id':1, 'name': 'XYZ', 'email': "XYZ@xyz.com", 'is_admin': True},
        {'id':2, 'name': 'ABC', 'email': "ABC@abc.com", 'is_admin': False},
        {'id':3, 'name': 'MNO', 'email': "MNO@mno.cpm", 'is_admin': False}
    ]

    logger.debug(f'Total Records: {len(data)}')
    return jsonify({'result': data, "status": 200})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')