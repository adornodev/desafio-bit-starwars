import json

from flask import make_response
from app.models.response import Response
from app.helpers.json_encoder import CustomJSONEncoder

def send_response(result:Response):

    resp = make_response(json.dumps(result.to_dict(), cls=CustomJSONEncoder))
    resp.mimetype = 'application/json'
    return resp