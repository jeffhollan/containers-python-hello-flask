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
    app.logger.info('container called')
    return f"hello from python flask! container id: {os.getenv('POD_NAME')} at internal ip {os.getenv('POD_IP')}"
app.run(host='0.0.0.0')