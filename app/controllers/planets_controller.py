import requests

from flask import request
from app.models.planet import Planet
from app.models.response import Response
from app import mongo
from app.helpers.request_utils import send_response
from bson import ObjectId

def index():
  # Get pagination parameters
  page = int(request.args.get('page', 1))
  page_size = int(request.args.get('page_size', 5))

  page = 1 if page < 1 else page
  page_size = 5 if page_size < 5 else page_size
  
  # Find planets on db
  planets_db = list(mongo.db.planets.find({}, projection=Planet.remove_invisible_fields(ignore_id=False)).sort([('name', 1)]).skip((page-1) * page_size).limit(page_size))

  return send_response(Response(True, data=planets_db))

def show(planet_id):
  # Build query
  query = None
  if planet_id.isdigit():
    query = {'swapi_id': int(planet_id)}
  elif ObjectId.is_valid(planet_id):
    query = {'_id': ObjectId(str(planet_id))}
  else:
    query = {'name': planet_id}


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

  # Search if this planet already registered on database
  planet_on_db = mongo.db.planets.find_one({'name': planet.name})
  if planet_on_db:
    return send_response(Response(False, f'The planet "{planet.name}" has already been registered in our database'))

  # Call SWAPI to get more data
  query_params = {'search': planet.name}
  swapi_response = requests.get('https://swapi.co/api/planets/', query_params)

  # Try to get id and films from SWAPI
  if swapi_response.status_code == 200:
    json_resp = swapi_response.json()
    if 'count' in json_resp and json_resp['count'] > 0:
      planet_data     = next(filter(lambda x: x['name'].upper() == planet.name.upper(), json_resp['results']))
      planet.films    = len(planet_data['films'])
      planet.swapi_id = int(list(filter(None, planet_data['url'].split('/')))[-1])
    else:
      return send_response(Response(False, 'This planet does not exist'))

  # Insert Planet on mongo
  res = mongo.db.planets.insert_one(planet.to_dict())

  return send_response(Response(res.acknowledged))


def destroy():
  payload = request.get_json(force=True)

  # Build query
  query = None
  if 'name' in payload:
    query = {'name': payload['name']}
  elif 'swapi_id' in payload:
    query = {'swapi_id': int(payload['swapi_id'])}
  elif '_id' in payload:
    query = {'_id': ObjectId(str(payload['id']))}
  else:
    return send_response(Response(False, "It's necessary to provider \"_id\", \"swapi_id\" or \"name\" field to remove planet from database" ))

  # Delete from database
  resp = mongo.db.planets.delete_many(query)

  if resp.deleted_count < 1:
    return send_response(Response(False, 'This planet is not registered in our database to remove it'))

  return send_response(Response(True))