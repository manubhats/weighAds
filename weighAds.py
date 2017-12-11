from flask import Flask
from flask import render_template, request
import logging
from logging.handlers import RotatingFileHandler
from wpt_api import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submitURL', methods=['POST'])
def submit_url():
    url = request.form["url"]
    wpt = WPTApi()
    print(url)


if __name__ == '__main__':
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host='0.0.0.0', debug=True)
