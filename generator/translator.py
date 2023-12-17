import json

from generator.components import Functions, Blocks


class Translator:
    
    def __init__(self, dictionary = None):
        self.__functions  = None
        self.__blocks = None
        self._update_dict(dictionary)

    def translate(self, raw_data):
        mid_stage = raw_data
        for function, trans in self.__functions.items():
            mid_stage = mid_stage.replace(trans, function)
        # TODO: Make translation of blocks
        return mid_stage 

    def _update_dict(self, dictionary):
        if dictionary is None:
            dictionary = 'dictionary.json'
        self._load_json(dictionary)

    def _load_functions(self, functions_data):
        functions_fields = Functions.get_fields()
        if len(functions_data) != len(functions_fields):
            raise Exception("Fields of 'functions' does not match")
        for field in functions_fields:
            if field.name not in functions_data:
                raise Exception(f"Missing function '{field.name}' in dictionary")

        for function, trans in functions_data.items():
            if not trans:
                functions_data[function] = function
        
        self.__functions = Functions(**functions_data)
        

    def _load_blocks(self, blocks_data):
        pass

    def _load_json(self, dictionary):
        with open(dictionary) as dict_file:
            json_data = json.load(dict_file)
        self._load_functions(json_data["functions"])
        self._load_blocks(json_data["blocks"])