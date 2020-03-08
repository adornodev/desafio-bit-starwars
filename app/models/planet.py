from app import mongo
from .base_model import BaseModel

class Planet(BaseModel):

    def __init__(self, name = '', climate = '', terrain = ''):
        super().__init__()
        self.name = name
        self.climate = climate
        self.terrain = terrain

    @classmethod
    def get(self):
        return []

planet_model=Planet()