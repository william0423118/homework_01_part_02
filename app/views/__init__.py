from app import flask_app as app
import json
from datetime import datetime
from flask import request, jsonify
import numpy as np


@app.route("/heartbeat")
def heartbeat():
    return json.dumps(
        {
            "status": True,
            "service": "Homework_Template",
            "datetime": f"{datetime.now()}"
        }
    )


@app.route('/sum/<resp>', methods = ['GET', 'POST'])
def sum(resp):
    data = request.json
    #print (data['x'])
    sum_ = {'result': data['x'] + data['y']}
    return jsonify(sum_)

@app.route('/minimum/<resp>', methods = ['GET', 'POST'])
def minimum(resp):
    data = request.json
    #print (data['x'])
    min_ = {'result': min(data['values'])}
    return jsonify(min_)

@app.route('/product/<resp>', methods = ['GET', 'POST'])
def product(resp):
    data = request.json
    #print (data['x'])
    if len(data['values']) == 0:
        return jsonify(0)
    else:
        min_ = {'result': int(np.prod(data['values']))}
        return jsonify(min_)

@app.before_first_request
def load_app():
    print("Loading App Before First Request")
