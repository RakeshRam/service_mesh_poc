import sys
import logging

from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)

CORS(app)

logger = logging.getLogger('App Name: Contact Service - V1')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.route('/contact')
def contact():
    logger.info("Demo view: contact page")
    logger.debug('App Version: V1')
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')