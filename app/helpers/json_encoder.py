import json
from datetime import datetime
from bson import ObjectId

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return str(o.isoformat())
        return json.JSONEncoder.default(self, o)