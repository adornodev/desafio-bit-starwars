from datetime import datetime
from flask_pymongo import ObjectId

class BaseModel(object):
  def __init__(self):
    self.created_at = datetime.utcnow()
    self.updated_at = datetime.utcnow()
    self._id = ObjectId()