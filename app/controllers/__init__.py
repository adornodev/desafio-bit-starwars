import os
from flask import Blueprint

from app.controllers.planets_controller import index as planets_index
from app.controllers.planets_controller import destroy as planets_destroy



planet_blueprints = Blueprint('planets', 'api', url_prefix='/planets')
planet_blueprints.add_url_rule('/<int:planet_id>', view_func=planets_index, methods=['GET'])
planet_blueprints.add_url_rule('/', view_func=planets_destroy, methods=['DELETE'])
