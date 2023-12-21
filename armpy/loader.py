import json


class ArmPy:
    
    def __init__(self, lang):
        self.__name__ = 'armpy'
        self.__all__ = []
        self.lang = lang
        self.__load()

    def __load(self):
        with open(f'armpy/dictionary.{self.lang}.json') as dict_file:
            functions = json.load(dict_file)['functions']
        for buitin_name, trans_name in functions.items():
            setattr(self, trans_name, globals()['__builtins__'][buitin_name])
            self.__all__.append(trans_name)
