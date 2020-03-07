from app import mongo

class Planet():

    def __init__(self):
        self.name = ''
        self.climate = ''
        self.terrain = ''

    @classmethod
    def get(self):
        return []

    @classmethod
    def getAllPosts(self):
        return []

planet_model=Planet()