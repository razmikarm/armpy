import json
from .generators import generate_function

class ArmPy:
    
    def __init__(self, lang):
        self.__name__ = 'armpy'
        self.__all__ = []
        self.lang = lang
        self.__load()

    def __load(self):
        with open(f'armpy/dictionary.{self.lang}.json') as dict_file:
            functions = json.load(dict_file)['functions']
        for buitin_name, translation in functions.items():
            args = None
            match translation:
                case "":
                    trans_name = buitin_name
                case str(trans_name):
                    pass
                case {
                    'name': str(trans_name),
                    'args': dict(args),
                }:
                    pass
            setattr(
                self,
                trans_name,
                generate_function(buitin_name, trans_name, arguments=args)
            )
            self.__all__.append(trans_name)
