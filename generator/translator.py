from generator.components import *

class Translator:
    
    def __init__(self, dictionary = None):
        self._update_dict(dictionary)
        self.tree = None

    def translate(self, raw_data):
        pass
    
    def _update_dict(self, dictionary):
        if dictionary is None:
            self.dict_data = self.load_json(dictionary)

    @classmethod
    def load_json(cls, dictionary):
        ...