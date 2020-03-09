import json
from .base_model import BaseModel

class Planet(BaseModel):

    def __init__(self, name='', climate= '', terrain= '', swapi_id= -1, films= -1):
        super().__init__()

        self.name = None if not name else name.strip()
        self.climate = [] if not climate else [climate] if ',' not in climate else [c.strip() for c in climate.split(',')]
        self.terrain = [] if not terrain else [terrain] if ',' not in terrain else [t.strip() for t in terrain.split(',')]
        self.swapi_id = swapi_id
        self.films = films

    def to_dict(self):
        result = {}
        
        result['name'] = self.name
        result['swapi_id'] = self.swapi_id
        result['films'] = self.films
        result['climate'] = self.climate
        result['terrain'] = self.terrain
        result['created_at'] = self.created_at
        result['updated_at'] = self.updated_at
        result['_id'] = self._id

        return result
    
    @staticmethod
    def remove_invisible_fields(ignore_id = True):
        fields = {'created_at': 0, 'updated_at': 0}

        if ignore_id:
            fields['_id'] = 0

        return fields

planet_model=Planet()