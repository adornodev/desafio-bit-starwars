from flask import request, jsonify
from app.models.planet import Planet
from app import mongo
from app.helpers.utils import send_response, bson_serialize

def index(planet_id):
  # Realizar pesquisa paginada no banco
  return send_response({'success': True})

def insert():
  payload = request.get_json(force=True)

  # Initialize a Planet object
  planet  = Planet(payload['name'], payload['climate'], payload['terrain'])

  # Insert Planet on mongo
  res = mongo.db.planets.insert_one(bson_serialize(planet))

  return send_response(planet)


def destroy():
  # Realizar leitura do req.body
  return send_response({'success': True})