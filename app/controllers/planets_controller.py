from flask import request, jsonify
from app.models.planet import Planet
from app import mongo

def index(planet_id):
  # Realizar pesquisa paginada no banco
  return jsonify({'success': True})

def destroy():
  # Realizar leitura do req.body
  return jsonify({'success': True})