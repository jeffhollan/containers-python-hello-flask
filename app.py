import json
import os
import requests
import logging
import flask
from flask import request, jsonify
from flask_cors import CORS

logging.basicConfig(level=logging.INFO)

# dapr_port = os.getenv("DAPR_HTTP_PORT")
# target_app = os.getenv("TARGET_APP")
# orders_url = "http://localhost:{}/v1.0/invoke/{}/method/store".format(dapr_port, target_app)

app = flask.Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST', 'GET'])
def neworder():
    # order = request.json
   # response = requests.post(orders_url, json=order, timeout=60)
    # log_string = "New order submitted, content: {content}".format(content = json.dumps(order))
    # app.logger.info(log_string)
    return 'hello flask'
app.run(host='0.0.0.0')