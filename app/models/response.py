class Response():
  def __init__(self, success, message = None, data = None):
    self.success = success
    self.message = message
    self.data = None if not data else data if isinstance(data, list) else [data]

    if not self.success and not self.message:
      self.message = 'Internal application processing error'

  def to_dict(self):
    result = {}

    result['success'] = self.success
    result['message'] = self.message
    result['data']    = self.data

    return result