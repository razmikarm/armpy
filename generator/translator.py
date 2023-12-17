import json

from generator.components import Functions, Blocks


class Translator:
    
    def __init__(self, dictionary = None):
        self._update_dict(dictionary)
        self.tree = None

    def translate(self, raw_data):
        pass

    def _update_dict(self, dictionary):
        if dictionary is None:
            dictionary = 'dictionary.json'
        self._load_json(dictionary)

    def _load_functions(self, functions_data):
        pass

    def _load_blocks(self, blocks_data):
        pass

    def _load_json(self, dictionary):
        with open(dictionary) as dict_file:
            json_data = json.load(dict_file)
        self._load_functions(json_data["functions"])
        self._load_blocks(json_data["blocks"])