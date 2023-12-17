from .translator import Translator


class Generator:

    def __init__(self, content, dictionary=None):
        self.raw_data = content
        self.__code = None
        self.translator = Translator(dictionary)

    @property
    def code(self):
        return self.__code

    def generate(self):
        self.__code = self.translator.translate(self.raw_data)
