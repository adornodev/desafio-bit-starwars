import json
from .base_model import BaseModel

class Planet(BaseModel):

    def __init__(self, name = '', climate = '', terrain = ''):
        super().__init__()
        self.name = name
        self.climate = climate
        self.terrain = terrain
    
    def to_dict(self):
        result = {}
        
        result['name'] = self.name
        result['climate'] = self.climate
        result['terrain'] = self.terrain
        result['created_at'] = self.created_at #str(self.created_at)
        result['updated_at'] = self.updated_at #str(self.updated_at)
        result['_id'] = self._id #str(self._id)

        return result
    
    @staticmethod
    def remove_invisible_fields(ignore_id = True):
        fields = {'created_at': 0, 'updated_at': 0}

        if ignore_id:
            fields['_id'] = 0

        return fields

planet_model=Planet()