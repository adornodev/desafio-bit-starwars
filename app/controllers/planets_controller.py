from flask import request
from app.models.planet import Planet
from app.models.response import Response
from app import mongo
from app.helpers.utils import send_response

def index():
  
  # Get pagination parameters
  page = int(request.args.get('page', 1))
  page_size = int(request.args.get('page_size', 5))

  page = 1 if page < 1 else page
  page_size = 5 if page_size < 5 else page_size
  
  # Find planets on db
  planets_db = list(mongo.db.planets.find({}, projection=Planet.remove_invisible_fields(ignore_id=False)).sort([('created_at', -1)]).skip((page-1) * page_size).limit(page_size))

  return send_response(Response(True, data=planets_db))

def show(planet_id):
  
  # Build query
  query = None
  if isinstance(planet_id, str):
    query = {'name': planet_id}
  elif isinstance(planet_id, ObjectId):
    query = {'_id': ObjectId(str(planet_id))}
  else:
    return send_response(Response(False, 'The input parameter can be string or ObjectId type'))
  
  # Search planet on mongo
  planet_on_db = mongo.db.planets.find_one(query, projection=Planet.remove_invisible_fields(ignore_id=False))

  if not planet_on_db:
    return send_response(Response(False, 'This planet is not registered in our database', data=planet_on_db))
  else:
    return send_response(Response(True, data=planet_on_db))

def insert():

  payload = request.get_json(force=True)

  # Initialize a Planet object
  planet = Planet(payload['name'], payload['climate'], payload['terrain'])

  # Insert Planet on mongo
  res = mongo.db.planets.insert_one(planet.to_dict())

  return send_response(Response(res.acknowledged))


def destroy():
  
  payload = request.get_json(force=True)

  # Build query
  query = None
  if 'name' in payload:
    query = {'name': payload['name']}
  elif 'id' in payload:
    query = {'_id': ObjectId(str(payload['id']))}
  else:
    return send_response(Response(False, "It's necessary to provider \"id\" or \"name\" field to remove planet from database" ))

  # Delete from database
  resp = mongo.db.planets.delete_many(query)

  if resp.deleted_count < 1:
    return send_response(Response(False, 'This planet is not registered in our database to remove it'))

  return send_response(Response(True))