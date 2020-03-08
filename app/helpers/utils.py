from flask import make_response, jsonify
from datetime import datetime
from flask_pymongo import ObjectId

def json_serialize(data):
    result = {}
    
    if isinstance(data, dict):
        result = data
    else:
        input_data = data.__dict__
        for prop in input_data:
            if isinstance(input_data[prop], (datetime, ObjectId)):
                result[prop] = str(input_data[prop])
            else:
                result[prop] = input_data[prop]

    return result

def bson_serialize(data):
    result = {}
    
    if isinstance(data, dict):
        result = data
    else:
        input_data = data.__dict__
        result = input_data

    return result

def send_response(result):
    resp = make_response(jsonify(json_serialize(result)))
    resp.mimetype = 'application/json'
    return resp